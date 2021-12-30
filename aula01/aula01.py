import pygame
# from pygame.locals import *
from sys import exit

from pygame.constants import QUIT


pygame.init()#Iniciando o Pygame

larguraTela = 640#largura da tela
alturaTela = 480#altura da tela
tela = pygame.display.set_mode((larguraTela,alturaTela))#definindo tela(largura, altura)
pygame.display.set_caption('Jogo')#titulo do jogo

while True:#loop principal, define se o jogo esta rodando
    for event in pygame.event.get():#captura os eventos do jogo
        if event.type  == QUIT:#saindo
            pygame.quit()
            exit()
    pygame.display.update()#atualizador de tela