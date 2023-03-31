import pygame
import random

pygame.init()

# Set screen size and title
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Turn-based game")

# Set font
pygame.font.init()
font = pygame.font.SysFont('SimHei', 24)

# Define classes for player and monster
class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10

    def attack(self, target):
        damage = random.randint(1, self.damage)
        print(f"{self.name} attacks {target.name} and deals {damage} damage!")
        target.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

class Monster:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, target):
        damage = random.randint(1, self.damage)
        print(f"{self.name} attacks {target.name} and deals {damage} damage!")
        target.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

# Define main class and GUI function
class Game:
    def __init__(self, player_name):
        self.player = Character(player_name)
        self.monster = Monster("Goblin", 50, 5)

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            # Update screen
            screen.fill((255, 255, 255))
            player_health_text = font.render(f"Player: {self.player.health}", True, (0, 0, 0))
            monster_health_text = font.render(f"{self.monster.name}: {self.monster.health}", True, (0, 0, 0))
            screen.blit(player_health_text, (10, 10))
            screen.blit(monster_health_text, (10, 40))
            pygame.display.flip()

            # Handle player input
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.player.attack(self.monster)
                if self.monster.health <= 0:
                    print(f"{self.monster.name} has been defeated!")
                    return

                self.monster.attack(self.player)
                if self.player.health <= 0:
                    print(f"{self.player.name} has been defeated!")
                    return

def GUI():
    game_instance = Game("Player")
    game_instance.start()

# Start the game
GUI()
