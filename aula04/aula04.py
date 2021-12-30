import pygame
from pygame.constants import * 

pygame.init()

larguraTela = 640
alturaTela = 480
x = larguraTela/2 - 40/2
y = alturaTela/2 - 50/2

tela = pygame.display.set_mode((larguraTela, alturaTela))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill('black')
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        # if event.type == KEYDOWN:
        #     if event.key == K_a:
        #         x = x - 20
        #     if event.key == K_d:
        #         x = x + 20
        #     if event.key == K_w:
        #         y = y - 20
        #     if event.key == K_s:
        #         y = y + 20

    if pygame.key.get_pressed()[K_a]:
        x -= 20
    if pygame.key.get_pressed()[K_d]:
        x += 20
    if pygame.key.get_pressed()[K_w]:
        y -= 20
    if pygame.key.get_pressed()[K_s]:
        y += 20


    retangulo = pygame.draw.rect(tela,(0,255,0),(x,y,40,50))


    pygame.display.update()