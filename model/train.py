import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
import argparse
import os

# ----------------------
# Parse command-line arguments
# ----------------------
parser = argparse.ArgumentParser()
parser.add_argument("--input_data", type=str, help="Path to input CSV")
parser.add_argument("--output_model", type=str, help="Directory to save the model")
args = parser.parse_args()

# ----------------------
# Load and preprocess data
# ----------------------
print(f"Reading input data from: {args.input_data}")
df = pd.read_csv(args.input_data)

print("🔄 Preprocessing training data...")
df.replace({"YES": 1, "NO": 0, "M": 1, "F": 0}, inplace=True)

if "LUNG_CANCER" in df.columns:
    df.rename(columns={"LUNG_CANCER": "label"}, inplace=True)

if "label" not in df.columns:
    raise ValueError("Target column 'label' not found after preprocessing.")

# ----------------------
# Split features and target
# ----------------------
X = df.drop("label", axis=1)
y = df["label"]

# ----------------------
# Train logistic regression model
# ----------------------
print("Training logistic regression model...")
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# ----------------------
# Save the model
# ----------------------
os.makedirs(args.output_model, exist_ok=True)
model_path = os.path.join(args.output_model, "model.joblib")
joblib.dump(model, model_path)
print(f"Model saved at: {model_path}")
