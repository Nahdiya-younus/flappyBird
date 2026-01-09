import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

gameWindow = pygame.display.set_mode((604, 500))
pygame.display.set_caption("Flappy Bird")

#define game variables
ground_scroll = 0 
scroll_speed = 4

#load images
bg = pygame.image.load("background.jpg")
ground_img = pygame.image.load("ground2.jpg")

class Brid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        
    
run = True 
#creating a game loop
while run:

    clock.tick(fps)

    #draw background
    gameWindow.blit(bg, (0,0))

    #draw and scroll the ground 
    gameWindow.blit(ground_img, (ground_scroll,375))
    ground_scroll -= scroll_speed 
    if abs(ground_scroll)> 55:
        ground_scroll = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()



