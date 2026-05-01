from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    # This works even though the route is in a router
    response = client.get("/") 
    assert response.status_code == 200
    assert response.json()["status"] == "online"

def test_read_item():
    response = client.get("/items/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "active": True}