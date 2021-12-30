import pygame
from sys import exit
from pygame.constants import QUIT
from pygame.draw import circle

pygame.init()

larguraTela = 640
alturaTela = 480

tela = pygame.display.set_mode((larguraTela,alturaTela))
pygame.display.set_caption('Jogo')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    retangulo = pygame.draw.rect(tela,(0,255,0),(200,300,40,50))
    #                            onde   (RGB)     (x, y , h, l)
    #                          aparece 
    circulo = pygame.draw.circle(tela,(0,0,255),(300,260), 40)
    #                            onde ,  (RGB),  (x, y),   r
    #                          aparece 
    linha = pygame.draw.line(tela, (255,255,0), (0,0),(640,480),80)
    #                        onde ,    (RGB)   ,(x, y),  (x,y)  espessura
    #                      aparece                PI      PF
    pygame.display.update()
    

#PI == Posição inicial
#PF == Posição final