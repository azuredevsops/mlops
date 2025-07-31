import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
import joblib
import argparse
import os

# ----------------------
# Parse command-line arguments
# ----------------------
parser = argparse.ArgumentParser()
parser.add_argument("--test_data", type=str, help="Path to test CSV")
parser.add_argument("--model_path", type=str, help="Path to model directory")
args = parser.parse_args()

# ----------------------
# Load test data
# ----------------------
print(f"Reading test data from: {args.test_data}")
df = pd.read_csv(args.test_data)

# Preprocess
print("Preprocessing test data...")
df.replace({"YES": 1, "NO": 0, "M": 1, "F": 0}, inplace=True)

if "LUNG_CANCER" in df.columns:
    df.rename(columns={"LUNG_CANCER": "label"}, inplace=True)

if "label" not in df.columns:
    raise ValueError("Target column 'label' not found in test data.")

X_test = df.drop("label", axis=1)
y_test = df["label"]

# ----------------------
# Load model
# ----------------------
model_file = os.path.join(args.model_path, "model.joblib")
print(f"Loading model from: {model_file}")
model = joblib.load(model_file)

# ----------------------
# Predict
# ----------------------
print("🔍 Running predictions...")
y_pred = model.predict(X_test)

# ----------------------
# Evaluate
# ----------------------
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
