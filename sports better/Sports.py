from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'
    id =
    username =
    balance =

class Player_prop(Base):
    __tablename__ = 'player_props'
    id =
    player_name =
    stat_type =
    stat_value =

class Bet(Base):
    __tablename__ = 'bets'
    id =
    user_id =
    player_id =
    bet_type =
    amount =
    status =