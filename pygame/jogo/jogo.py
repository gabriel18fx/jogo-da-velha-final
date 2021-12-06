import pygame
import sys
import time

from pygame import image

pygame.init()

size = width, height = 650, 650

screen = pygame.display.set_mode(size)

blak = 0, 0, 0
white = 255, 255, 255
x = 0

xis = pygame.image.load("xis.png")
bolinha = pygame.image.load("bolinha.png")

xis = pygame.transform.scale(xis, (100,100))
bolinha = pygame.transform.scale(bolinha, (100,100))

while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT): 
            sys.exit()

    if(x == 0):    
        screen.fill(white)
        x = 1
        screen.blit(xis, (0,0))
        screen.blit(xis, (100,100))
        screen.blit(xis, (0,200))
        screen.blit(xis, (200,0))
        screen.blit(xis, (200,200))
        
    else:
        screen.fill(blak)
        x = 0
        screen.blit(bolinha, (0,0))

    time.sleep(5)

    pygame.display.flip()