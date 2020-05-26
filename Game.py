import pygame
from Player import Player
from Monster import Monster

class Game():
    def __init__(self,surface):
        self.all_players = pygame.sprite.Group()
        self.player = Player(surface)
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.all_obstacles = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster(100, 100, 'ugo', 0.5)
        self.spawn_monster(1000, 0, 'victor', 0.2)
        self.spawn_monster(0, 750, 'paul', 0.4)

    def spawn_monster(self, x, y, name, velocity):
        monster = Monster(x, y, name, velocity)
        self.all_monsters.add(monster)
        self.all_monsters.add(monster)

    def delete(self, monster):
        self.all_monsters.remove(monster)

    def check_collison(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)