from fastapi import FastAPI

app = FastAPI()

# Dados fictícios dos álbuns do Megadeth
albuns = [
    {"album": "Rust in Peace", "ano": 1990, "destaque": "Holy Wars... The Punishment Due"},
    {"album": "Countdown to Extinction", "ano": 1992, "destaque": "Symphony of Destruction"},
]

@app.get("/")
def home():
    return {"mensagem": "API de Álbuns do Megadeth"}

@app.get("/albuns")
def get_albuns():
    return albuns

@app.get("/album/{nome}")
def get_album(nome: str):
    for album in albuns:
        if album["album"].lower() == nome.lower():
            return album
    return {"erro": "Álbum não encontrado"}
