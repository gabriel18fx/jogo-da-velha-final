import pygame
import sys
import time

from pygame import image

pygame.init()

size = width, height = 650, 650

screen = pygame.display.set_mode(size)



xis = pygame.image.load("xis.png")
bolinha = pygame.image.load("bolinha.png")

xis = pygame.transform.scale(xis, (100,100))
bolinha = pygame.transform.scale(bolinha, (100,100))

#varivais 
preto = 0, 0, 0
branco = 255, 255, 255
vermelho = 255, 0, 0
verde = 0, 255, 0
azul = 0, 0, 255

cores = [preto, branco, vermelho, verde, azul]


screen.fill(branco)
def desenha_quadro():
        pygame.draw.line(screen, preto, (200,0), (200,600),5)
        pygame.draw.line(screen, preto, (450,0), (450,600),5)
        pygame.draw.line(screen, preto, (0,200), (600,200),5)
        pygame.draw.line(screen, preto, (0,400), (600,400),5)


def xis_posi():
    screen.blit(xis, (50,50))
    screen.blit(xis, (275,50))
    screen.blit(xis, (480,50))
    screen.blit(xis, (50,250))
    screen.blit(xis, (275,250))
    screen.blit(xis, (480,250))
    screen.blit(xis, (50,475))
    screen.blit(xis, (275,475))
    screen.blit(xis, (480,475))

while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT): 
            sys.exit()

    desenha_quadro() 
    
    xis_posi()       

    pygame.display.flip()