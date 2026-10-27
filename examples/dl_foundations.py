import argparse
import json
import platform
import time

import torch
from sklearn.datasets import load_digits, make_moons
from sklearn.model_selection import train_test_split
from torch import nn
from torch.nn import functional as F


def train_classifier(model, x_train, y_train, x_val, y_val, epochs):
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    first_loss = None
    for _ in range(epochs):
        model.train()
        optimizer.zero_grad()
        loss = F.cross_entropy(model(x_train), y_train)
        loss.backward()
        optimizer.step()
        if first_loss is None:
            first_loss = loss.item()
    model.eval()
    with torch.no_grad():
        accuracy = (model(x_val).argmax(dim=1) == y_val).float().mean().item()
    return {"first_loss": round(first_loss, 4), "last_loss": round(loss.item(), 4), "validation_accuracy": round(accuracy, 4)}


def mlp(seed):
    x, y = make_moons(n_samples=400, noise=0.2, random_state=seed)
    x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.25, stratify=y, random_state=seed)
    tensors = [torch.tensor(v, dtype=torch.float32 if i < 2 else torch.long) for i, v in enumerate((x_train, x_val, y_train, y_val))]
    model = nn.Sequential(nn.Linear(2, 16), nn.ReLU(), nn.Linear(16, 2))
    return train_classifier(model, tensors[0], tensors[2], tensors[1], tensors[3], epochs=80)


def attention():
    torch.manual_seed(0)
    x = torch.randn(1, 4, 8)
    qkv = nn.Linear(8, 24, bias=False)
    q, k, v = qkv(x).chunk(3, dim=-1)
    scores = q @ k.transpose(-2, -1) / q.shape[-1] ** 0.5
    mask = torch.triu(torch.ones(4, 4, dtype=torch.bool), diagonal=1)
    weights = scores.masked_fill(mask, float("-inf")).softmax(dim=-1)
    actual = weights @ v
    expected = F.scaled_dot_product_attention(q, k, v, is_causal=True)
    torch.testing.assert_close(actual, expected, atol=1e-6, rtol=1e-5)
    assert weights[0, 0, 1:].sum().item() == 0
    return {"shape": list(actual.shape), "causal_future_weight": 0.0, "matches_pytorch_sdpa": True}


def gradient_check():
    torch.manual_seed(0)
    x = torch.randn(3, 2, dtype=torch.float64)
    w = torch.randn(2, 1, dtype=torch.float64, requires_grad=True)
    loss = (x @ w).square().mean()
    loss.backward()
    analytic = w.grad.clone()
    numeric = torch.zeros_like(w)
    epsilon = 1e-6
    with torch.no_grad():
        for i in range(w.shape[0]):
            w[i, 0] += epsilon
            plus = (x @ w).square().mean()
            w[i, 0] -= 2 * epsilon
            minus = (x @ w).square().mean()
            w[i, 0] += epsilon
            numeric[i, 0] = (plus - minus) / (2 * epsilon)
    torch.testing.assert_close(analytic, numeric, atol=1e-8, rtol=1e-5)
    return {"autograd_matches_finite_difference": True}


def cnn_vs_mlp(seed):
    digits = load_digits()
    x_train, x_val, y_train, y_val = train_test_split(
        digits.images / 16.0, digits.target, test_size=0.25, stratify=digits.target, random_state=seed
    )
    x_train = torch.tensor(x_train, dtype=torch.float32).unsqueeze(1)
    x_val = torch.tensor(x_val, dtype=torch.float32).unsqueeze(1)
    y_train, y_val = torch.tensor(y_train), torch.tensor(y_val)
    models = {
        "mlp": nn.Sequential(nn.Flatten(), nn.Linear(64, 64), nn.ReLU(), nn.Linear(64, 10)),
        "cnn": nn.Sequential(nn.Conv2d(1, 4, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2), nn.Flatten(), nn.Linear(4 * 4 * 4, 10)),
    }
    results = {}
    for name, model in models.items():
        started = time.perf_counter()
        result = train_classifier(model, x_train, y_train, x_val, y_val, epochs=30)
        result.update({"parameters": sum(p.numel() for p in model.parameters()), "cpu_seconds": round(time.perf_counter() - started, 3)})
        results[name] = result
    return {"dataset": "sklearn digits, identical split and full-batch budget", "epochs_per_model": 30, "results": results}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("task", choices=["mlp", "attention", "gradient", "cnn"])
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    torch.manual_seed(args.seed)
    torch.set_num_threads(1)
    result = {"python": platform.python_version(), "torch": torch.__version__, "device": "cpu", "seed": args.seed}
    tasks = {"mlp": mlp, "attention": attention, "gradient": gradient_check, "cnn": cnn_vs_mlp}
    task = tasks[args.task]
    result.update(task(args.seed) if args.task in {"mlp", "cnn"} else task())
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
