import copy
import io
import json
import platform
import threading
import time

import psutil
import sklearn
import torch
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from torch import nn
from torch.nn import functional as F

SEED = 42


class Int8WeightOnlyLinear(nn.Module):
    def __init__(self, source):
        super().__init__()
        scale = source.weight.abs().amax(dim=1).clamp(min=1e-12) / 127
        self.register_buffer("weight_int8", torch.round(source.weight / scale[:, None]).clamp(-127, 127).to(torch.int8))
        self.register_buffer("scale", scale)
        self.register_buffer("bias", source.bias.detach().clone())
        self.logical_parameters = source.weight.numel() + source.bias.numel()

    def forward(self, x):
        return F.linear(x, self.weight_int8.float() * self.scale[:, None], self.bias)


def quantize_weight_only(model):
    quantized = copy.deepcopy(model)
    for name, module in quantized.named_modules():
        if isinstance(module, nn.Linear):
            parent = quantized
            parts = name.split(".")
            for part in parts[:-1]:
                parent = getattr(parent, part)
            setattr(parent, parts[-1], Int8WeightOnlyLinear(module))
    quantized.logical_parameters = sum(p.numel() for p in model.parameters())
    return quantized


def measure(model, x, y):
    process = psutil.Process()
    batch = x[:16]
    model.eval()
    with torch.inference_mode():
        for _ in range(10):
            model(batch)
    rss_samples = []
    stop = threading.Event()

    def sample_rss():
        while not stop.is_set():
            rss_samples.append(process.memory_info().rss)
            time.sleep(0.0005)

    baseline_rss = process.memory_info().rss
    sampler = threading.Thread(target=sample_rss)
    sampler.start()
    started = time.perf_counter()
    with torch.inference_mode():
        for _ in range(50):
            model(batch)
    elapsed = time.perf_counter() - started
    with torch.inference_mode():
        predictions = model(x).argmax(dim=1)
    stop.set()
    sampler.join()
    state = io.BytesIO()
    torch.save(model.state_dict(), state)
    return {
        "accuracy": round((predictions == y).float().mean().item(), 4),
        "state_dict_bytes": len(state.getvalue()),
        "batch16_latency_ms": round(elapsed / 50 * 1000, 3),
        "peak_rss_delta_bytes_during_inference": max(rss_samples or [baseline_rss]) - baseline_rss,
    }


def main():
    torch.manual_seed(SEED)
    torch.set_num_threads(1)
    digits = load_digits()
    x_train, x_test, y_train, y_test = train_test_split(
        digits.data / 16.0, digits.target, test_size=0.25, stratify=digits.target, random_state=SEED
    )
    x_train, x_test = torch.tensor(x_train, dtype=torch.float32), torch.tensor(x_test, dtype=torch.float32)
    y_train, y_test = torch.tensor(y_train), torch.tensor(y_test)
    models = {}
    for name, width in [("baseline_width64", 64), ("compact_width16", 16)]:
        model = nn.Sequential(nn.Linear(64, width), nn.ReLU(), nn.Linear(width, 10))
        optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
        for _ in range(30):
            optimizer.zero_grad()
            loss = F.cross_entropy(model(x_train), y_train)
            loss.backward()
            optimizer.step()
        models[name] = model
    models["baseline_int8_weight_only"] = quantize_weight_only(models["baseline_width64"])
    results = {}
    for name, model in models.items():
        results[name] = measure(model, x_test, y_test)
        results[name]["logical_parameters"] = getattr(model, "logical_parameters", sum(p.numel() for p in model.parameters()))
    print(json.dumps({
        "python": platform.python_version(),
        "torch": torch.__version__,
        "sklearn": sklearn.__version__,
        "device": "cpu",
        "seed": SEED,
        "comparison": "same train/test split and 30 full-batch epochs for learned models; PTQ is applied to baseline",
        "latency": "50 timed batch-16 runs after 10 warmups; single CPU thread; full-test accuracy evaluated outside the timing loop",
        "memory": "process RSS sampled every 0.5 ms during inference; delta from pre-measurement RSS, not a hardware peak guarantee",
        "results": results,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
