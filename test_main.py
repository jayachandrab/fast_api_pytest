from fastapi.testclient import TestClient
from .main import app, todos

# importing the module
import pytest


client = TestClient(app)


def setup_function():
    todos.clear()


def test_read_todos():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == []


def test_create_todos():
    response = client.post(
        '/', json={"name": "Buy groceries", "completed": False})
    assert response.status_code == 200
    assert response.json() == {"name": "Buy groceries", "completed": False}

def test_update_todos():
    client.post(
        '/', json={"name": "Buy groceries", "completed": False})
    response = client.put('/1',json={"name": "Buy groceries", "completed": True})
    assert response.status_code == 200
    print(response.json())
    assert response.json() == {"name": "Buy groceries", "completed": True}

def test_delete_todos():
    client.post(
        '/', json={"name": "Buy groceries", "completed": False})
    response = client.delete('/1')
    assert response.status_code == 200
    assert response.json() == {"name": "Buy groceries", "completed": False}