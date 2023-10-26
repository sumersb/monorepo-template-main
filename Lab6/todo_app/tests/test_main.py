import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming your FastAPI app is in a file named "app.py"

# Create a TestClient instance
client = TestClient(app)

def test_first_api():
    response = client.get("/api")
    assert response.json() == {"msg": "hello_world"}

def test_first_apiV2():
    response = client.get("/books/4n3x")  # Replace with an actual path_param value
    assert response.json() == {"msg": "4n3x"}

def test_first_apiV3():
    response = client.get("/books/?title=sumer%20is%20a%20cool%20guy")  # Replace with an actual title value
    assert response.json() == {"msg": "sumer is a cool guy"}

def test_first_apiV4():
    data = {"abc": "def"}  # Replace with the data you want to send
    response = client.post("/books/create_book", json=data)
    assert response.json() == {"msg": {"abc": "def"}}

def test_first_apiV5():
    response = client.put("/books/freshfrog")  # Replace with an actual path_param value
    assert response.json() == {"msg": "freshfrog"}

def test_first_apiV6():
    response = client.delete("/books/abacus")  # Replace with an actual path_param value
    assert response.json() == {"msg": "abacus"}