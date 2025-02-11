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
    def __init__(self, name, level, hp, attack, defense, speed, moves):
        self.name = name
        self.level = level
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.moves = moves  # List of Move objects

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def is_fainted(self):
        return self.hp <= 0

    def attack_opponent(self, move, opponent):
        damage = max(1, move.power + self.attack - opponent.defense)
        opponent.take_damage(damage)
        return damage

    def get_move(self):
        return random.choice(self.moves)

    def battle_ui(pokemon1, pokemon2):
        screen.fill(255,255,255)
        screen.blit(pokemon1.image, (50,250))
        screen.blit(pokemon2.image, (500,50))

        draw_hp_bar(pokemon1, 50, 350)
        draw_hp_bar(pokemon2, 500, 150)

        pygame.display.update()

    def draw_hp_bar(pokemon, x, y):
        ratio = pokemon.hp/pokemon.max_hp
        pygame.draw.rect(screen,)
        
class Player:
    def

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()
