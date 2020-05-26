import pygame
from math import *
from Game import Game
from random import randint

pygame.init()

surface = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
surfaceL = surface.get_width()
surfaceH = surface.get_height()

nb_joysticks = pygame.joystick.get_count()
#On compte les joysticks
nb_joysticks = pygame.joystick.get_count()
#Et on en crée un s'il y a en au moins un
if nb_joysticks > 0:
    mon_joystick = pygame.joystick.Joystick(0)
    mon_joystick.init()  # Initialisation

input = {'inputR': pygame.K_RIGHT, 'inputL': pygame.K_LEFT, 'inputU': pygame.K_UP, 'inputD': pygame.K_DOWN}

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

game = Game(surface)

surface.fill(white)
pygame.display.update()

continuer = True
while continuer:
    surface.fill(white)
    surface.blit(game.player.image,game.player.rect)
    game.all_monsters.draw(surface)
    for monster in game.all_monsters:
        rect2 = monster.collid_rect
        pygame.draw.rect(surface, red, rect2, 2)
    pygame.display.update()

    for monster in game.all_monsters:
        print(monster.name)
        if game.check_collison(monster,game.all_monsters):
            monster.follow(game.player, game, surface)

    if game.pressed.get(input['inputR']) and game.player.rect.x<1138:
        game.player.move_right()
    if game.pressed.get(input['inputL']) and game.player.rect.x>0:
        game.player.move_left()
    if game.pressed.get(input['inputU']) and game.player.rect.y>0:
        game.player.move_up()
    if game.pressed.get(input['inputD']) and game.player.rect.y<670:
        game.player.move_down()

    game.player.move_joy(game,input)
    # if not (game.pressed.get(inputR) or game.pressed.get(inputL)):
    #     if abs(game.player.moveX) > 0.2:
    #         game.player.posX += game.player.moveX*game.player.velocity
    # if not (game.pressed.get(inputU) or game.pressed.get(inputD)):
    #     if abs(game.player.moveY) > 0.2:
    #         game.player.posY += game.player.moveY*game.player.velocity

    game.player.rect.x = game.player.posX
    game.player.rect.y = game.player.posY

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
            pygame.quit()
            quit()

        if event.type == pygame.JOYAXISMOTION:
            if event.axis == 0:
                game.player.moveX = event.value
            if event.axis == 1:
                game.player.moveY = event.value

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            game.pressed[event.key] = True

        if event.type == pygame.KEYUP:
            game.pressed[event.key] = False