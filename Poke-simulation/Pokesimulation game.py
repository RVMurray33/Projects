import pygame as pygame

Frames = 60
Clock =

Pokedex = {
    "Bulbasaur" : 1,
    "Ivysaur" : 2,
    "Venusaur" : 3,
    "Charmander" : 4,
    "Charmeleon" : 5,
    "Charizard" : 6,
    "Squirtle" : 7,
    "Wartortle" : 8,
    "Blastoise" : 9,
}

class Pokemon:
    def stats(self, health, attack, sp_attack, defense, sp_defense, accuracy):
        self.health = health
        self.attack = attack
        self.sp_attack = sp_attack
        self.defense = defense
        self.sp_defense = sp_defense
        self.accuracy = accuracy

class Player:
    def

pygame.