"""Testes para a API FastAPI da discografia do Megadeth."""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_discografia():
    """Testa o endpoint /discografia."""
    response = client.get("/discografia")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_album():
    """Testa o endpoint /album/{ano}."""
    response = client.get("/album/1992")
    assert response.status_code == 200
    assert response.json()["album"] == "Countdown to Extinction"

def test_read_musicas():
    """Testa o endpoint /musicas/{album}."""
    response = client.get("/musicas/Rust%20in%20Peace")
    assert response.status_code == 200
    assert isinstance(response.json()["musicas"], list)

def test_filter_albums_by_year():
    """Testa o endpoint /albuns/?ano=."""
    response = client.get("/albuns/?ano=1990")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert response.json()[0]["album"] == "Rust in Peace"

def test_search_albums_by_keyword():
    """Testa o endpoint /busca/?keyword=."""
    response = client.get("/busca/?keyword=rust")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert response.json()[0]["album"] == "Rust in Peace"

def test_create_album():
    """Testa o endpoint POST /album/."""
    new_album = {"album": "Test Album", "ano": 2023, "destaque": "Test Song",
                 "musicas": ["Test Song 1", "Test Song 2"]}
    response = client.post("/album/", json=new_album)
    assert response.status_code == 200
    assert response.json()["album"] == new_album

def test_update_album():
    """Testa o endpoint PUT /album/{album_nome}."""
    updated_album = {"album": "Updated Album", "ano": 2024, "destaque": "Updated Song",
                     "musicas": ["Updated Song 1", "Updated Song 2"]}
    response = client.put("/album/Rust%20in%20Peace", json=updated_album)
    assert response.status_code == 200
    assert response.json()["album"] == updated_album

def test_get_album_details():
    """Testa o endpoint /album_detalhes/{album_nome}."""
    response = client.get("/album_detalhes/Rust%20in%20Peace")
    assert response.status_code == 200
    assert response.json()["album"] == "Rust in Peace"

def test_get_albums_by_year_range():
    """Testa o endpoint /albuns_por_intervalo/?ano_inicio=&ano_fim=."""
    response = client.get("/albuns_por_intervalo/?ano_inicio=1990&ano_fim=1992")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 2

def test_get_destaque_album():
    """Testa o endpoint /destaque/{album_nome}."""
    response = client.get("/destaque/Rust%20in%20Peace")
    assert response.status_code == 200
    assert response.json()["destaque"] == "Holy Wars... The Punishment Due"