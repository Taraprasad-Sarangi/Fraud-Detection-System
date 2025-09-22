from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Dict
from utils import load_artifacts, preprocess_one

app = FastAPI(title="Fraud Detection API", version="0.1.0")
model, scaler = load_artifacts()

class Transaction(BaseModel):
    Time: float
    Amount: float
    # V1..V28 as floats
    V1: float;  V2: float;  V3: float;  V4: float;  V5: float;  V6: float;  V7: float
    V8: float;  V9: float;  V10: float; V11: float; V12: float; V13: float; V14: float
    V15: float; V16: float; V17: float; V18: float; V19: float; V20: float; V21: float
    V22: float; V23: float; V24: float; V25: float; V26: float; V27: float; V28: float

@app.get("/")
def root():
    return {"ok": True, "service": "fraud-detection", "version": "0.1.0"}

@app.post("/predict")
def predict(tx: Transaction) -> Dict:
    x = preprocess_one(tx.model_dump(), scaler)
    proba = float(model.predict_proba(x)[0,1])
    pred = int(proba >= 0.5)
    return {"fraud_probability": proba, "is_fraud": pred, "threshold": 0.5}
