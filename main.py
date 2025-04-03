from fastapi import FastAPI
from typing import List

app = FastAPI()

discografia_megadeth = [
    {"album": "Rust in Peace", "ano": 1990, "destaque": "Holy Wars... The Punishment Due", "musicas": ["Holy Wars... The Punishment Due", "Hangar 18", "Take No Prisoners"]},
    {"album": "Countdown to Extinction", "ano": 1992, "destaque": "Symphony of Destruction", "musicas": ["Symphony of Destruction", "Sweating Bullets", "Skin o' My Teeth"]},
    {"album": "Peace Sells... but Who's Buying?", "ano": 1986, "destaque": "Peace Sells", "musicas": ["Peace Sells", "Wake Up Dead", "Black Friday"]},
    {"album": "Youthanasia", "ano": 1994, "destaque": "A Tout Le Monde", "musicas": ["A Tout Le Monde", "Train of Consequences", "Reckoning Day"]},
    {"album": "Endgame", "ano": 2009, "destaque": "Head Crusher", "musicas": ["This Day We Fight! ", "44 Minutes", "EndGame"]},
    {"album": "Thirdeen", "ano": 2011, "destaque": "FastLane", "musicas": ["New World Order", "Black Swan", "Fast Lane"]},
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
