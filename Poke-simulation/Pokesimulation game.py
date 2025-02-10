import pygame as pygame

pygame.init()

WIDTH, HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pokemon Simulation"))
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
    def stats(self, health, attack, sp_attack, defense, sp_defense, speed):
        self.health = health
        self.attack = attack
        self.sp_attack = sp_attack
        self.defense = defense
        self.sp_defense = sp_defense
        self.speed = speed

class Player:
    def

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()
