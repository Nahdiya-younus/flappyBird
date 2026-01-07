import pygame
from pygame.locals import *

pygame.init()

gameWindow = pygame.display.set_mode((604, 500))
pygame.display.set_caption("Flappy Bird")

#load images
bg = pygame.image.load("background.jpg")
ground_img = pygame.image.load("ground1.jpg")

run = True 
#creating a game loop
while run:

    #draw background
    gameWindow.blit(bg, (0,0))

    #draw and scroll the ground 
    gameWindow.blit(ground_img, (0,350))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()



