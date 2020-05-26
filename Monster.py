import pygame
from random import *

class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, name, velocity):
        super().__init__()
        self.name = name
        self.image = pygame.image.load('perso_f.png')
        self.rect = self.image.get_rect()
        self.collid_rect = pygame.Rect(x, y+self.rect.h*3/4, self.rect.w, self.rect.h/4)
        self.x = x
        self.y = y
        self.velocity = velocity * randint(1,4)/2

    def follow(self, player, game, surf):
        collision = {'gauche': False, 'droite': False, 'haut': False, 'bas': False, }
        for monster in game.all_monsters:
            if monster.name != self.name:
                monster_rect = monster.collid_rect
                if self.collid_rect.clip(monster_rect).left == self.collid_rect.left \
                        and self.collid_rect.clip(monster_rect).w != 0:
                    collision['gauche'] = True
                if self.collid_rect.clip(monster_rect).right == self.collid_rect.right \
                        and self.collid_rect.clip(monster_rect).w != 0:
                    collision['droite'] = True
                if self.collid_rect.clip(monster_rect).top == self.collid_rect.top \
                        and self.collid_rect.clip(monster_rect).h != 0:
                    collision['haut'] = True
                if self.collid_rect.clip(monster_rect).bottom == self.collid_rect.bottom \
                        and self.collid_rect.clip(monster_rect).h != 0:
                    collision['bas'] = True

        if player.rect.x < self.rect.x and not collision['gauche']:
            self.x -= self.velocity
        elif player.rect.x > self.rect.x and not collision['droite']:
            self.x += self.velocity

        if player.rect.y < self.rect.y and not collision['haut']:
            self.y -= self.velocity
        elif player.rect.y > self.rect.y and not collision['bas']:
            self.y += self.velocity

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        self.collid_rect.x = self.rect.x
        self.collid_rect.y = self.rect.y+self.rect.h*3/4