import requests

def test_predict_smoke():
    sample = {"Time":100,"Amount":10}
    for i in range(1,29): sample[f"V{i}"]=0.0
    r = requests.post("http://127.0.0.1:8000/predict", json=sample, timeout=5)
    assert r.status_code == 200
    out = r.json()
    assert "fraud_probability" in out and "is_fraud" in out
