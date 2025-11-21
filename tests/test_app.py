import pytest
from app import app   # assuming your app code is in app.py

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome" in response.data

def test_hello_default(client):
    response = client.get("/hello")
    assert response.status_code == 200
    assert b"Hello, Guest!" in response.data

def test_hello_with_name(client):
    response = client.get("/hello?name=Anand")
    assert response.status_code == 200
    assert b"Hello, Anand!" in response.data

def test_echo_post(client):
    response = client.post("/echo", json={"msg": "Hi"})
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data == {"you_sent": {"msg": "Hi"}}
