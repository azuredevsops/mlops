import joblib
import numpy as np

# ----------------------
# Load model once (when container starts)
# ----------------------
def init():
    global model
    model = joblib.load("model.joblib")
    print("Model loaded.")

# ----------------------
# Called when a request is made
# ----------------------
def run(raw_data):
    try:
        data = np.array(raw_data["data"])
        preds = model.predict(data)
        return {"predictions": preds.tolist()}
    except Exception as e:
        return {"error": str(e)}
