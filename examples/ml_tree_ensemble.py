import json
import platform

import sklearn
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import AdaBoostClassifier, HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

SEED = 42
X, y = load_breast_cancer(return_X_y=True)
X_train, X_holdout, y_train, y_holdout = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=SEED
)
X_fit, X_val, y_fit, y_val = train_test_split(
    X_train, y_train, test_size=0.25, stratify=y_train, random_state=SEED
)
models = {
    "tree_depth_3": DecisionTreeClassifier(max_depth=3, random_state=SEED),
    "random_forest": RandomForestClassifier(n_estimators=100, random_state=SEED, n_jobs=1),
    "adaboost": AdaBoostClassifier(n_estimators=50, random_state=SEED),
    "gradient_boosting": HistGradientBoostingClassifier(max_iter=100, random_state=SEED),
}
rows = {}
for name, model in models.items():
    model.fit(X_fit, y_fit)
    pred = model.predict(X_val)
    prob = model.predict_proba(X_val)[:, 1]
    rows[name] = {
        "validation_accuracy": round(accuracy_score(y_val, pred), 4),
        "validation_roc_auc": round(roc_auc_score(y_val, prob), 4),
    }
print(json.dumps({
    "python": platform.python_version(),
    "sklearn": sklearn.__version__,
    "seed": SEED,
    "split_sizes": {"fit": len(y_fit), "validation": len(y_val), "holdout": len(y_holdout)},
    "results": rows,
    "holdout_used": False,
}, indent=2, sort_keys=True))
