import pygame
from sys import exit
from pygame.constants import QUIT
from pygame.draw import circle

pygame.init()

larguraTela = 640
alturaTela = 480
x = larguraTela/2 - 40/2
y = 0

tela = pygame.display.set_mode((larguraTela,alturaTela))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()#objeto pra controlar os frames

while True:
    relogio.tick(30)#frames
    tela.fill(('black'))#muda de cor quando não tem obj nenhum no espaço
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    retangulo = pygame.draw.rect(tela,(0,255,0),(x,y,40,50))
    if y >= alturaTela:
        y=0
        
    y += 5#passos

    pygame.display.update()
    