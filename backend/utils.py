import joblib
import numpy as np

# Lazy-load for speed when imported
_model = None
_scaler = None

def load_artifacts(model_path="../models/fraud_model.pkl", scaler_path="../models/scaler.pkl"):
    global _model, _scaler
    if _model is None:
        _model = joblib.load(model_path)
    if _scaler is None:
        _scaler = joblib.load(scaler_path)
    return _model, _scaler

def preprocess_one(sample: dict, scaler):
    """
    sample is a dict with keys: Time, Amount, V1..V28
    Returns a 2D array [ [features...] ] in correct order
    """
    order = ["Time","Amount"] + [f"V{i}" for i in range(1,29)]
    x = np.array([sample[k] for k in order], dtype=float).reshape(1,-1)

    # scale time & amount (cols 0,1)
    x_scaled = x.copy()
    x_scaled[:, :2] = scaler.transform(x[:, :2])
    return x_scaled
