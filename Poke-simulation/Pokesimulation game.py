from fastapi import FastAPI, HTTPException
import requests
import random


app = FastAPI()

active_battle = None

class Pokemon:
    def __init__(self, name, hp, attack, defense, speed, moves, type):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.moves = moves
        self.type = type
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        
    def fainted(self):
        return self.hp <= 0

def get_pokemon(name: str):
    url = f"https:pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Pokémon not found"}

    data = response.json()

    stats = {stat["stat"]["name"]: stat["base_stat"] for stat in data ["stats"]}

    moves = {}
    for move in data["moves"][:4]:
        move_name = move["move"]["name"]
        move_url = move["move"]["url"]
        move_data = requests.get(move_url).json()
        move_power = move_data.get("power", 40)
        moves[move_name] = move_power

    return {
        "hp": stats["hp"],
        "attack": stats["attack"],
        "defense": stats["defense"],
        "speed": stats["speed"],
        "moves": moves,
        "type": data["types"][0]["type"]["name"],
        "sprite": data["sprites"]["front_default"]
    }

@app.get("/pokemon/{name}")
def get_pokemon_api(name: str):
    pkmn_data = get_pokemon(name)
    if pkmn_data is None:
        raise HTTPException(status_code=404, detail="Pokémon not found")

@app.post("/start_battle/")
def battle(player_pokemon: str, opponent_pokemon: str):
    global active_battle

    p1_data = get_pokemon(player_pokemon)
    p2_data = get_pokemon(opponent_pokemon)

@app.post("/attack/")
def select_move(self, player_pokemon):
    pokemon_data = get_pokemon(player_pokemon)
