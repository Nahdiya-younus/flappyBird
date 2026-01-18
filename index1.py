import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 604
screen_height = 500

gameWindow = pygame.display.set_mode((604, 500))
pygame.display.set_caption("Flappy Bird")

#define game variables
ground_scroll = 0 
scroll_speed = 4
flying = False
game_over = False
pipe_gap = 100

#load images
bg = pygame.image.load("background.jpg")
ground_img = pygame.image.load("ground2.jpg")

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1,4):
            img  = pygame.image.load(f'bird{num}.png')
            self.images.append(img)

        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.vel = 0
        self.clicked = False


    def update(self):

        if flying == True:
            # gravity
            self.vel += 0.2
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 375:
                self.rect.y += int(self.vel)
        if game_over == False:
            #jump
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False :
                self.clicked = True
                self.vel = -6
            if pygame.mouse.get_pressed()[0] == 0 :
                self.clicked = False

            #handle the animation
            self.counter += 1
            flap_cooldown = 5

            if self.counter > flap_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index  =0
            self.image = self.images[self.index]

            #rotate the bird
            self.image = pygame.transform.rotate(self.images[self.index], self.vel*-2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('pipe.png')
        self.rect = self.image.get_rect()
        #position 1 is from the top, -1 is from the bottom
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft =[x, y-int(pipe_gap / 2)]
        if position == -1:
            self.rect.topleft = [x, y + int(pipe_gap / 2)]

    def update(self):
        self.rect.x -= scroll_speed

brid_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

flappy = Bird(100,int(screen_height / 2))

brid_group.add(flappy)

btm_pipe = Pipe(300, int(screen_height / 2), -1 )
top_pipe = Pipe(300, int(screen_height / 2), 1 )
pipe_group.add(btm_pipe)
pipe_group.add(top_pipe)
           
run = True 
#creating a game loop
while run:

    clock.tick(fps)

    #draw background
    gameWindow.blit(bg, (0,0))

    brid_group.draw(gameWindow)
    brid_group.update()
    pipe_group.draw(gameWindow)
    pipe_group.update()

    #draw the ground
    gameWindow.blit(ground_img, (ground_scroll,375))

    # check if bird has hit the ground
    if flappy.rect.bottom > 375 :
        game_over = True
        flying = False

    if game_over == False:
    #draw and scroll the ground 
        ground_scroll -= scroll_speed 
        if abs(ground_scroll)> 55:
            ground_scroll = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True

    pygame.display.update()

pygame.quit()



