from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_main_root():
    expected = {"Hello": "World"}
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == expected