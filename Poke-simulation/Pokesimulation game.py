import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/pokemon/{name}")
def get_pokemon(name: str):
    url = f"https:pokeapi.co/api/v2/pokemon/{name.lower()}"
    requests = requests.get(url)

    if response.status_code != 200:
        return {error}
