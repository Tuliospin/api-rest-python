from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_register():
    response = client.post("/auth/register", json={
        "name": "Test User",
        "email": "test@example.com",
        "password": "secret123"
    })
    assert response.status_code in (201, 400)  # 400 if already exists


def test_login_invalid():
    response = client.post("/auth/login", json={
        "email": "notfound@example.com",
        "password": "wrongpass"
    })
    assert response.status_code == 401


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "docs" in response.json()
