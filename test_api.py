from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_discografia():
    response = client.get("/discografia")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_album():
    response = client.get("/album/1992")
    assert response.status_code == 200
    assert response.json()["album"] == "Countdown to Extinction"

def test_read_musicas():
    response = client.get("/musicas/Rust%20in%20Peace")
    assert response.status_code == 200
    assert isinstance(response.json()["musicas"], list)

def test_filter_albums_by_year():
    response = client.get("/albuns/?ano=1990")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert response.json()[0]["album"] == "Rust in Peace"

def test_search_albums_by_keyword():
    response = client.get("/busca/?keyword=rust")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert response.json()[0]["album"] == "Rust in Peace"

def test_create_album():
    new_album = {"album": "Test Album", "ano": 2023, "destaque": "Test Song", "musicas": ["Test Song 1", "Test Song 2"]}
    response = client.post("/album/", json=new_album)
    assert response.status_code == 200
    assert response.json()["album"] == new_album

def test_update_album():
    updated_album = {"album": "Updated Album", "ano": 2024, "destaque": "Updated Song", "musicas": ["Updated Song 1", "Updated Song 2"]}
    response = client.put("/album/Rust%20in%20Peace", json=updated_album)
    assert response.status_code == 200
    assert response.json()["album"] == updated_album

def test_get_album_details():
    response = client.get("/album_detalhes/Rust%20in%20Peace")
    assert response.status_code == 200
    assert response.json()["album"] == "Rust in Peace"

def test_get_albums_by_year_range():
    response = client.get("/albuns_por_intervalo/?ano_inicio=1990&ano_fim=1992")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 2

def test_get_destaque_album():
    response = client.get("/destaque/Rust%20in%20Peace")
    assert response.status_code == 200
    assert response.json()["destaque"] == "Holy Wars... The Punishment Due"