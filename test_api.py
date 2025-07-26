from fastapi.testclient import TestClient
from iris_fastapi import app  # Change to match your FastAPI script filename

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]

def test_prediction():
    sample_input = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    response = client.post("/predict/", json=sample_input)
    assert response.status_code == 200
    assert response.json()["predicted_class"] in ["setosa", "versicolor", "virginica"]

