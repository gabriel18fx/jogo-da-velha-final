from os import link
from typing import Collection
import pygame
import sys
import time

from pygame import image
from pygame import transform

pygame.init()

size = width, height = 600, 600

screen = pygame.display.set_mode(size)

xis = pygame.image.load("xis.png")
bolinha = pygame.image.load("bolinha.png")
jogada = 0

xis = pygame.transform.scale(xis, (100,100))
bolinha = pygame.transform.scale(bolinha, (100,100))

jogadores = [xis, bolinha]

jogadores_paralelos = ['X','O']

#varivais 
preto = 0, 0, 0
branco = 255, 255, 255
vermelho = 255, 0, 0
verde = 0, 255, 0
azul = 0, 0, 255
cores = [preto, branco, vermelho, verde, azul]

quadrante_linha = [50, 245, 450]
quadrante_coluna = [50, 245, 450]

linhau = [' ',' ',' ']
linhad = [' ',' ',' ']
linhat = [' ',' ',' ']

matriz_paralela = [linhau,
                   linhad,
                   linhat]

screen.fill(cores[1])

jogador_vez = 0
ganhador = 0

def desenha_quadro():
    pygame.draw.line(screen, preto, (200,0), (200,600),6)
    pygame.draw.line(screen, preto, (400,0), (400,600),6)
    pygame.draw.line(screen, preto, (0,200), (600,200),6)
    pygame.draw.line(screen, preto, (0,400), (600,400),6)



def faz_jogada(pos, vez_jogador):
    index_linha = int(pos[0]/200)
    index_coluna = int(pos[1]/200)
    if(matriz_paralela[index_coluna][index_linha] == ' '):
        matriz_paralela[index_coluna][index_linha] = jogadores_paralelos[vez_jogador]
        print("---------------")
        print(linhau)
        print(linhad)
        print(linhat)
        print("---------------")
        screen.blit(jogadores[vez_jogador],(quadrante_linha[index_linha], quadrante_coluna[index_coluna]))
    else:
        print("Ocupado")

def ganhou():
 for i in range(0):
        if matriz_paralela[0][0]==matriz_paralela[0][1]=='X' and matriz_paralela[0][0]==matriz_paralela[0][2] =='X':
            pygame.draw.line(screen, azul,(0,100), [600,100], 10)
            return 1
        elif matriz_paralela[1][0]==matriz_paralela[1][1]=='X' and matriz_paralela[1][0]==matriz_paralela[1][2] =='X':
            pygame.draw.line(screen, azul,(0,300), [600,300], 10)
            return 1
        elif matriz_paralela[2][0]==matriz_paralela[2][1]=='X' and matriz_paralela[2][0]==matriz_paralela[2][2]=='X':
            pygame.draw.line(screen, azul,(0,500), [600,500], 10)
            return 1
        elif matriz_paralela[0][0]==matriz_paralela[1][0]=='X' and matriz_paralela[0][0]==matriz_paralela[2][0]=='X':
            pygame.draw.line(screen, azul,(100,0), [100,600], 10)
            return 1
        elif matriz_paralela[0][1]==matriz_paralela[1][1]=='X' and matriz_paralela[0][1]==matriz_paralela[2][1]=='X':
            pygame.draw.line(screen, azul,(300,0), [300,600], 10)
            return 1
        elif matriz_paralela[0][2]==matriz_paralela[1][2]=='X' and matriz_paralela[0][2]==matriz_paralela[2][2]=='X':
            pygame.draw.line(screen, azul,(500,0), [500,600], 10)
            return 1
        elif matriz_paralela[0][0]==matriz_paralela[1][1]=='X' and matriz_paralela[0][0]==matriz_paralela[2][2]=='X':
            pygame.draw.line(screen, azul,(0,0), [600,600], 10)
            return 1
        elif matriz_paralela[0][2]==matriz_paralela[1][1]=='X' and matriz_paralela[0][2]==matriz_paralela[2][0]=='X':
            pygame.draw.line(screen,  azul,(600,0), [0,600], 10)
            return 1

        if matriz_paralela[0][0]==matriz_paralela[0][1]== 'O' and matriz_paralela[0][0]==matriz_paralela[0][2] =='O':
            pygame.draw.line(screen, vermelho,(0,300), [600,300], 10)
            return 2
        elif matriz_paralela[1][0]==matriz_paralela[1][1]=='O' and matriz_paralela[1][0]==matriz_paralela[1][2] =='O':
            pygame.draw.line(screen, vermelho,(0,300), [600,300], 10)
            return 2
        elif matriz_paralela[2][0]==matriz_paralela[2][1]=='O' and matriz_paralela[2][0]==matriz_paralela[2][2]=='O':
            pygame.draw.line(screen, vermelho,(0,500), [600,500], 10)
            return 2
        elif matriz_paralela[0][0]==matriz_paralela[1][0]=='O' and matriz_paralela[0][0]==matriz_paralela[2][0]=='O':
            pygame.draw.line(screen, vermelho,(100,0), [100,600], 10)
            return 2
        elif matriz_paralela[0][1]==matriz_paralela[1][1]=='O' and matriz_paralela[0][1]==matriz_paralela[2][1]=='O':
            pygame.draw.line(screen, vermelho,(300,0), [300,600], 10)
            return 2
        elif matriz_paralela[0][2]==matriz_paralela[1][2]=='O' and matriz_paralela[0][2]==matriz_paralela[2][2]=='O':
            pygame.draw.line(screen, vermelho,(500,0), [500,600], 10)
            return 2
        elif matriz_paralela[0][0]==matriz_paralela[1][1]=='O' and matriz_paralela[0][0]==matriz_paralela[2][2]=='O':
            pygame.draw.line(screen, vermelho,(0,0), [600,600], 10)
            return 2
        elif matriz_paralela[0][2]==matriz_paralela[1][1]=='O' and matriz_paralela[0][2]==matriz_paralela[2][0]=='O':
            pygame.draw.line(screen, vermelho,(600,0), [0,600], 10)
            return 2
            


while True:
    desenha_quadro()
    ganhador = ganhou()
    for event in pygame.event.get():
        if (event.type == pygame.QUIT): 
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()
            faz_jogada(click_pos, jogador_vez)
            print(ganhador)

            if(jogador_vez == 0):jogador_vez = 1
            elif(jogador_vez == 1): jogador_vez = 0
        


    pygame.display.flip()
