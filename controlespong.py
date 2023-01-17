from pplay.window import *
from pplay.sprite import *
import pygame
from pygame.locals import *
from sys import exit


altura = 625
largura = 1000
janela = Window(largura, altura)
janela.set_title("Football Pong")
Mouse = Window.get_mouse()
teclado = Window.get_keyboard()

campo = Sprite("imagenspong/football-field.png")

teclas = Sprite("imagenspong/teclas.png")
teclas.x = 190
teclas.y = 180

caixona = Sprite("imagenspong/caixona.jpg")
caixona.x = 100
caixona.y = 40

retornar = Sprite("imagenspong/caixinha.jpg")
retornar.x = largura - 420
retornar.y = altura - 120

teclado1 = Sprite("imagenspong/keyboard.png")
teclado1.x = largura//4 - 40
teclado1.y = altura//2 - 220

teclado2 = Sprite("imagenspong/keyboard.png")
teclado2.x = largura*3//4 - 60
teclado2.y = altura//2 - 220

fonte2 = pygame.font.SysFont('malgungothicsemilight',40,True,False)
fonte4 = pygame.font.SysFont('malgungothicsemilight',30,True,False)

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Football Pong")
relogio = pygame.time.Clock()
pygame.init()

def controles():
    clique = 60
    janela.update()

    while True:

        voltar = 'VOLTAR'
        esquerdo = 'BRASIL'
        direito = 'ARGENTINA'


        voltar_formatado = fonte2.render(voltar, True, (255, 255, 255))
        esquerdo_formatado = fonte4.render(esquerdo, True, (255, 255, 255))
        direito_formatado = fonte4.render(direito, True, (255,255,255))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        if Mouse.is_over_object(retornar):
            voltar_formatado = fonte2.render(voltar, True, (218, 165, 32))

        if Mouse.is_button_pressed(1) and clique == 0:
            if Mouse.is_over_object(retornar):
                return

        if clique > 0:
            clique -= 1

        if teclado.key_pressed("ESC"):
            return

        campo.draw()
        caixona.draw()
        retornar.draw()
        teclado1.draw()
        teclado2.draw()
        teclas.draw()
        tela.blit(voltar_formatado,(largura - 300,altura- 110))
        tela.blit(direito_formatado,(largura*3//4 - 110, altura //2 - 260 ))
        tela.blit(esquerdo_formatado,(largura//4 - 50, altura//2 - 260))
        pygame.display.flip()