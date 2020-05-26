import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,surface):
        super().__init__()
        surfaceL = surface.get_width()
        self.velocity = 3
        self.image = pygame.image.load('pnj_armure.png')
        self.image = pygame.transform.scale(self.image, (int(surfaceL/50), int(surfaceL/40)))
        self.rect = self.image.get_rect()
        self.posX = 200.000
        self.posY = 200.000
        self.moveX = 0
        self.moveY = 0

    def move_right(self):
        self.posX += self.velocity

    def move_left(self):
        self.posX -= self.velocity

    def move_up(self):
        self.posY -= self.velocity

    def move_down(self):
        self.posY += self.velocity

    def move_joy(self,game,input):
        if not (game.pressed.get(input['inputR']) or game.pressed.get(input['inputL'])):
            if abs(self.moveX) > 0.2:
                self.posX += self.moveX * self.velocity
        if not (game.pressed.get(input['inputU']) or game.pressed.get(input['inputD'])):
            if abs(self.moveY) > 0.2:
                self.posY += self.moveY * self.velocity

        self.rect.x = self.posX
        self.rect.y = self.posY