from fastapi import APIRouter
import random

router = APIRouter()

active_battles = {}

@router.post("/battle/start")
def start_battle(player_pokemon: str, opponent_pokemon: str):
  player_data = get_pokemon(player_pokemon)
  opponent_data = get_pokemon(opponent_pokemon)
