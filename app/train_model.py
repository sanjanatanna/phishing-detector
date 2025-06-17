# app/train_model.py
import pandas as pd
import joblib
from scipy.sparse import load_npz
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import classification_report

print("📦 Loading vectorized features...")
X = load_npz("data/features.npz")

y = pd.read_csv("data/y_labels.csv")['label']

print("🔀 Splitting dataset...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define models
models = {
    "LogisticRegression": LogisticRegression(max_iter=1000),
    "RandomForest": RandomForestClassifier(n_estimators=100),
    "GradientBoosting": GradientBoostingClassifier(n_estimators=100),
}

best_model = None
best_f1 = 0

print("🧠 Training models...")
for name, model in models.items():
    print(f"\n⏳ Training: {name}")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred, output_dict=True)
    f1 = report['weighted avg']['f1-score']
    print(classification_report(y_test, y_pred))

    if f1 > best_f1:
        best_model = model
        best_f1 = f1
        best_name = name

print(f"\n🏆 Best model: {best_name} with F1-score = {best_f1:.4f}")
joblib.dump(best_model, "models/best_model.joblib")
print("✅ Saved best model.")
