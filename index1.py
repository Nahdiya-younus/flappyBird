import pygame
from pygame.locals import *

pygame.init()

gameWindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("Flappy Bird")


run = True 

#creating a game loop
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



