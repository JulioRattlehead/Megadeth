from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "API de Álbuns do Megadeth"}

def test_get_albuns():
    response = client.get("/albuns")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_album():
    response = client.get("/album/Rust in Peace")
    assert response.status_code == 200
    assert response.json()["album"] == "Rust in Peace"

def test_get_album_not_found():
    response = client.get("/album/Inexistente")
    assert response.status_code == 200
    assert "erro" in response.json()
