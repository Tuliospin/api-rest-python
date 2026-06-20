from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_items_requires_auth():
    response = client.get("/items/")
    assert response.status_code == 401


def test_create_item_requires_auth():
    response = client.post("/items/", json={"title": "Test", "price": 9.99})
    assert response.status_code == 401
