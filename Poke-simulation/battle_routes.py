from fastapi import APIRouter
import random

router = APIRouter()

active_battles = {}

@router.post("/battle/start")
def start_battle(player_pokemon: str, opponent_pokemon: str):
  player_data = get_pokemon(player_pokemon)
  opponent_data = get_pokemon(opponent_pokemon)

  battle_id = random.randint(1000,9999)
def get_speed(player_data, opponent_data)
  if player_data["stats"]["speed"] > opponent_data["stats"]["speed"]:
    turn = player_data
  else:
    turn = opponent_data
  return turn
  active_battles[battle_id] = {
    "player": player_data,
    "oppponent": opponent_data,
    "turn": turn
  }

  @router.post("/battle/finished")
  def end_battle(player_pokemon: str, opponent_pokemon: str):
    player_data = get_pokemon(player_pokemon)
    opponent_data = get_pokemon(opponent_pokemon)

    if len(opponent.party) = 0
    active_battle = 0

    return {"battle_id": battle_id, "message": "Battle started!"}

@router.post("/battle/attack")
def attack(player_pokemon: str, opponent_pokemon: str):
  player_data =

@router.post("/battle/items")
def use_item(player_inventory):
  if player 
