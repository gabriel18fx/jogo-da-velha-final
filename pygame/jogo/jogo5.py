from os import link, truncate
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
velha = pygame.image.load("velha.jpg")
jogadas = 0

xis = pygame.transform.scale(xis, (100,100))
bolinha = pygame.transform.scale(bolinha, (100,100))

jogadores = [xis, bolinha]

jogadores_paralelos = ['X','O']
teste = False
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

def desenha_quadro():
    pygame.draw.line(screen, preto, (200,0), (200,600),6)
    pygame.draw.line(screen, preto, (400,0), (400,600),6)
    pygame.draw.line(screen, preto, (0,200), (600,200),6)
    pygame.draw.line(screen, preto, (0,400), (600,400),6)






def vitoria():
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
        

def jogadas_1(pos):    
    index_coluna= int(pos[0]/200)
    index_linha= int(pos[1]/200)
    if matriz_paralela[index_linha][index_coluna] ==' ': 
        screen.blit(xis,(quadrante_linha[index_coluna],quadrante_coluna[index_linha]))
        matriz_paralela[index_linha][index_coluna] = 'X'
        print("---------------")
        print(linhau)
        print(linhad)
        print(linhat)
        print("---------------")
        return 0
    else:
        print("posicao ja ocupada!")           
        return -1

   
def jogadas_2(pos):
        index_coluna= int(pos[0]/200)
        index_linha = int(pos[1]/200)
        if matriz_paralela[index_linha][index_coluna]==' ':
            screen.blit(bolinha,(quadrante_linha[index_coluna],quadrante_coluna[index_linha]))
            matriz_paralela[index_linha][index_coluna] = 'O'
            print("---------------")
            print(linhau)
            print(linhad)
            print(linhat)
            print("---------------")
            return 0
        
        else:
            print("posicao ocupada!")
            return -1


while not teste:
    ganhador = 0
    soma = 0
    mouse_pos = pygame.mouse.get_pos() 
    desenha_quadro()  

      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             done = True
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos  = pygame.mouse.get_pos()   


            if ( jogadas%2== 0):
                soma = jogadas_1(click_pos)
                jogadas = jogadas + 1 + soma
                ganhador = vitoria()
                if ganhador == 1:
                    print('Vitoria do jogador X')
                    done = True
                    vencedor = 100
                if ganhador == 2:
                    print('Vitoria do jogador O')
                    vencedor = 100
                    done = True
            elif (  jogadas%2 == 1):
                soma = jogadas_2(click_pos)
                jogadas = jogadas + 1 + soma
                ganhador = vitoria()
            
            if jogadas >=9:
                screen.fill(branco)
                screen.blit(velha,(200,250)) 
                break
            
            
        

    
    pygame.display.flip()