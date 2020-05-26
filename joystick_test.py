import pygame
from random import *
from numpy import *
surfaceL = 1600
surfaceH = 900

pygame.init()
nb_joysticks = pygame.joystick.get_count()
print("Il y a", nb_joysticks, "joystick(s) branché(s)")
#On compte les joysticks
nb_joysticks = pygame.joystick.get_count()
#Et on en crée un s'il y a en au moins un
if nb_joysticks > 0:
    mon_joystick = pygame.joystick.Joystick(0)

    mon_joystick.init() #Initialisation

print("Axes :", mon_joystick.get_numaxes())
print("Boutons :", mon_joystick.get_numbuttons())
print("Trackballs :", mon_joystick.get_numballs())
print("Hats :", mon_joystick.get_numhats())

while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            print("je capte un truc")
        if event.type == pygame.JOYAXISMOTION:
            if event.value < -0.2 or event.value > 0.2:
               if event.axis == 0:
                   print("n°0")
               if event.axis == 1:
                   print("n°1")
               if event.axis == 2:
                   print("n°2")
               if event.axis == 3:
                   print("n°3")
               if event.axis == 4:
                   print("n°4")