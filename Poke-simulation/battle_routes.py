from fastapi import APIRouter
import random

router = APIRouter()

active_battles = {}

@router.post("/battle/start")
def start_battle(player_pokemon: str, opponent_pokemon: str):
  player_data = get_pokemon(player_pokemon)
  opponent_data = get_pokemon(opponent_pokemon)

  battle_id = random.randint(1000,9999)
  active_battles[battle_id] = {
    "player": player_data,
    "oppponent": opponent_data,
    "turn": "player"
  }

  return {"battle_id": battle_id, "message": "Battle started!"}
