#Criado por João Pedro Silva de Sá

#Pequeno briefing:
#A ideia desse jogo veio do jogo Pong (1972) com a temática moderna de copa do mundo


import pygame
from pplay.window import *
from pplay.sprite import *
from pplay.mouse import *
import random
import controlespong
import jogosolopong
import jogosduopong

altura = 625
largura = 1000
janela = Window(largura, altura)
janela.set_title("Football Pong")
Mouse = Window.get_mouse()
background = Sprite("imagenspong/menu.jpg")
espaco1 = Sprite("imagenspong/caixinha.jpg")
espaco1.x = largura - 520
espaco1.y = 160
espaco2 = Sprite("imagenspong/caixinha.jpg")
espaco2.x = largura - 520
espaco2.y = 260
espaco4 = Sprite("imagenspong/caixinha.jpg")
espaco4.x = largura - 520
espaco4.y = 360
som = Sprite("imagenspong/som.png")
som.x = 20
som.y = altura - 60
off = Sprite("imagenspong/X.png")
off.x = 20
off.y = altura-60
off.hide()

fonte1 = pygame.font.SysFont('malgungothicsemilight',80,True,False)
fonte2 = pygame.font.SysFont('malgungothicsemilight',40,True,False)
fonte3 = pygame.font.SysFont('malgungothicsemilight',15,True,False)

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Football Pong")
relogio = pygame.time.Clock()
barulho_clique = pygame.mixer.Sound('trilhapong/Apito Jogo.mp3')
barulho_clique.set_volume(0.3)
pygame.mixer.music.set_volume(0.5)
musica_de_fundo = pygame.mixer.music.load("trilhapong/Shakira - Waka Waka.mp3")
pygame.mixer.music.play(-1)
barulho = 1
clique = 60
janela.update()
while True:
    tela.fill((0, 0, 0))
    titulo = f"FOOTBALL PONG"
    jogarsolo = f'JOGO SOLO'
    jogarduo = f'JOGO 1X1'
    controles = f'CONTROLES'
    info1 = f'Aperte M para remover o som'
    info2 = f'Aperte U para voltar o som'

    titulo_formatado = fonte1.render(titulo, True, (218, 165, 32))
    jogarsolo_formatado = fonte2.render(jogarsolo, True, (255, 255, 255))
    jogaarduo_formatado = fonte2.render(jogarduo, True, (255, 255, 255))
    controles_formatado = fonte2.render(controles, True, (255, 255, 255))
    info1_formatado = fonte3.render(info1, True,(255,255,255))
    info2_formatado = fonte3.render(info2, True, (255,255,255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_m:
                pygame.mixer.music.pause()
                off.unhide()
                barulho = 0
            if event.key == K_u:
                pygame.mixer.music.unpause()
                off.hide()
                barulho = 1


    if Mouse.is_over_object(espaco1):
        jogarsolo_formatado = fonte2.render(jogarsolo, True, (218, 165, 32))
    if Mouse.is_over_object(espaco2):
        jogaarduo_formatado = fonte2.render(jogarduo, True, (218, 165, 32))
    if Mouse.is_over_object(espaco4):
        controles_formatado = fonte2.render(controles, True, (218, 165, 32))

    if Mouse.is_button_pressed(1) and clique == 0:
        if Mouse.is_over_object(espaco1):
            if barulho == 1:
                barulho_clique.play()
            janela.update()
            jogosolopong.jogosolo(barulho)
        if Mouse.is_over_object(espaco2):
            if barulho == 1:
                barulho_clique.play()
            janela.update()
            jogosduopong.jogoduo(barulho)
        if Mouse.is_over_object(espaco4):
            janela.update()
            controlespong.controles()
    if clique>0:
        clique -= 1


    janela.set_background_color((0, 0, 0))
    background.draw()
    espaco1.draw()
    espaco2.draw()
    espaco4.draw()
    som.draw()
    off.draw()
    tela.blit(titulo_formatado, (largura//2 - 385, 5))
    tela.blit(jogarsolo_formatado, (largura - 500, 170))
    tela.blit(jogaarduo_formatado, (largura - 500, 270))
    tela.blit(controles_formatado, (largura - 500, 370))
    tela.blit(info1_formatado, (largura - 250, altura - 60))
    tela.blit(info2_formatado, (largura - 250, altura - 35))
    janela.update()