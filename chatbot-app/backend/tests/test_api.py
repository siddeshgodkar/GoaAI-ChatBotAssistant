from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "FastAPI chatbot running 🚀"}

def test_chat_endpoint():
    response = client.post("api/chat", json={"message":"hi"})
    assert response.status_code == 200
    assert "reply" in response.json()