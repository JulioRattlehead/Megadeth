from fastapi import FastAPI, Query
from typing import List, Optional

app = FastAPI()

discografia_megadeth = [
    {"album": "Rust in Peace", "ano": 1990, "destaque": "Holy Wars... The Punishment Due", "musicas": ["Holy Wars... The Punishment Due", "Hangar 18", "Take No Prisoners"]},
    {"album": "Countdown to Extinction", "ano": 1992, "destaque": "Symphony of Destruction", "musicas": ["Symphony of Destruction", "Sweating Bullets", "Skin o' My Teeth"]},
    {"album": "Peace Sells... but Who's Buying?", "ano": 1986, "destaque": "Peace Sells", "musicas": ["Peace Sells", "Wake Up Dead", "Black Friday"]},
    {"album": "Youthanasia", "ano": 1994, "destaque": "A Tout Le Monde", "musicas": ["A Tout Le Monde", "Train of Consequences", "Reckoning Day"]},
    {"album": "Dystopia", "ano": 2016, "destaque": "Dystopia", "musicas": ["Dystopia", "The Threat Is Real", "Fatal Illusion"]},
]

@app.get("/discografia", response_model=List[dict])
async def read_discografia():
    return discografia_megadeth

@app.get("/album/{ano}")
async def read_album(ano: int):
    for album in discografia_megadeth:
        if album["ano"] == ano:
            return album
    return {"message": "Álbum não encontrado"}

@app.get("/musicas/{album}")
async def read_musicas(album: str):
    for disco in discografia_megadeth:
        if disco["album"] == album:
            return {"musicas": disco["musicas"]}
    return {"message": "Album não encontrado"}

@app.get("/albuns/")
async def filter_albums_by_year(ano: int = Query(..., description="Ano de lançamento do álbum")):
    filtered_albums = [album for album in discografia_megadeth if album["ano"] == ano]
    if filtered_albums:
        return filtered_albums
    return {"message": f"Nenhum álbum encontrado para o ano {ano}"}

@app.get("/busca/")
async def search_albums_by_keyword(keyword: str = Query(..., description="Palavra-chave no título do álbum")):
    filtered_albums = [album for album in discografia_megadeth if keyword.lower() in album["album"].lower()]
    if filtered_albums:
        return filtered_albums
    return {"message": f"Nenhum álbum encontrado com a palavra-chave '{keyword}'"}

@app.post("/album/")
async def create_album(album: dict):
    discografia_megadeth.append(album)
    return {"message": "Álbum adicionado com sucesso", "album": album}

@app.put("/album/{album_nome}")
async def update_album(album_nome: str, album_atualizado: dict):
    for i, album in enumerate(discografia_megadeth):
        if album["album"] == album_nome:
            discografia_megadeth[i] = album_atualizado
            return {"message": f"Álbum '{album_nome}' atualizado com sucesso", "album": album_atualizado}
    return {"message": f"Álbum '{album_nome}' não encontrado"}

@app.get("/album_detalhes/{album_nome}")
async def get_album_details(album_nome: str):
    for album in discografia_megadeth:
        if album["album"] == album_nome:
            return album
    return {"message": f"Álbum '{album_nome}' não encontrado"}

@app.get("/albuns_por_intervalo/")
async def get_albums_by_year_range(ano_inicio: int = Query(..., description="Ano de início do intervalo"), ano_fim: int = Query(..., description="Ano de fim do intervalo")):
    filtered_albums = [album for album in discografia_megadeth if ano_inicio <= album["ano"] <= ano_fim]
    if filtered_albums:
        return filtered_albums
    return {"message": f"Nenhum álbum encontrado no intervalo de anos {ano_inicio} - {ano_fim}"}

@app.get("/destaque/{album_nome}")
async def get_destaque_album(album_nome: str):
    for album in discografia_megadeth:
        if album["album"] == album_nome:
            return {"destaque": album["destaque"]}
    return {"message": f"Álbum '{album_nome}' não encontrado"}