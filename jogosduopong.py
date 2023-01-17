import pygame
from pplay.window import *
from pplay.sprite import *
from pplay.mouse import *

altura = 625
largura = 1000
janela = Window(largura, altura)
janela.set_title('Sá Pong')

teclado = Window.get_keyboard()
#Tamanho pixels 100x100
bola = Sprite("imagenspong/brazuca.png")
lenxb = 100
lenyb = 100
maraca = Sprite("imagenspong/maraca.jpg")
pad1 = Sprite("imagenspong/chuteiraesquerda.png")
pad2 = Sprite("imagenspong/chuteiradireita.png")
brasil = Sprite("imagenspong/bandeira br.jpg")
brasil.x = 310
brasil.y = 15
argentina = Sprite("imagenspong/bandeira arg.jpg")
argentina.x = 630
argentina.y = 20
pad2.x = largura - 66
finalargentina = Sprite("imagenspong/argentina campeã.png")
finalbrasil=Sprite("imagenspong/brasilcampeao.jpg")
mensagemcaixa = Sprite("imagenspong/caixa.jpg")
mensagemcaixa.x = 50
mensagemcaixa.y = 20
caixamenu = Sprite("imagenspong/caixinhamenor.jpg")
caixamenu.x = 50
caixamenu.y = altura - 110
caixarestart = Sprite("imagenspong/caixinhamenor.jpg")
caixarestart.x = 510
caixarestart.y = altura - 110

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Jogo")
relogio = pygame.time.Clock()

fonte = pygame.font.SysFont('adobe gothic std kalin',40,True,False)

pygame.init()
gol_brasil = pygame.mixer.Sound('trilhapong/Gol-Brasil.mp3')
gol_argentina = pygame.mixer.Sound('trilhapong/Grito-Gol.mp3')
Mouse = Window.get_mouse()

def jogoduo(barulho):
    velocidade = 500
    velx = 320
    vely = 320

    pontoesq = -1
    pontodir = 0
    bola.x = 600
    bola.y = altura // 2 - 300
    fim = False
    colisoes = 0
    clique = 60
    janela.update()
    while True:
        mensagem = f'BRA {pontoesq} x {pontodir} ARG'
        texto_formatado = fonte.render(mensagem, False, (255, 255, 255))
        ret_texto = texto_formatado.get_rect()
        ret_texto.center = (largura // 2, altura // 2)
        if teclado.key_pressed("w"):
            if pad1.y <= 0:
                pass
            else:
                pad1.y += -velocidade*janela.delta_time()
        if teclado.key_pressed("s"):
            if pad1.y >= altura - 100:
                pass
            else:
                pad1.y += velocidade*janela.delta_time()
        if teclado.key_pressed("UP"):
            if pad2.y <= 0:
                pass
            else:
                pad2.y += -velocidade*janela.delta_time()
        if teclado.key_pressed("DOWN"):
            if pad2.y >= altura - 100:
                pass
            else:
                pad2.y += velocidade*janela.delta_time()


    
        bola.move_x(velx*janela.delta_time())
        bola.move_y(vely*janela.delta_time())
        #x += velx
        #y += vely
        if bola.collided(pad1):
            bola.x = pad1.width + 1
            if colisoes <= 12:
                velx = -velx * 1.1
            else:
                velx = -velx
            colisoes += 1
        if bola.collided(pad2):
            bola.x = largura - (100 + pad2.width)
            if colisoes <= 12:
                velx = -velx*1.1
            else:
                velx = -velx
            colisoes += 1
        if bola.x > largura - pad2.width//2:
            bola.x = largura/2
            pontoesq += 1
            if barulho == 1:
                gol_brasil.play()
            velx = 320
            colisoes = 0
        if bola.y >= altura-100:
            bola.y = altura - 100
            vely = -vely
        if bola.x <= 0:
            bola.x = largura/2
            pontodir += 1
            if barulho == 1:
                gol_argentina.play()
            velx = 320
            colisoes = 0
        if bola.y <= 0:
            bola.y = 100
            vely = -vely
    
        if pontoesq == 5:
            fonte5 = pygame.font.SysFont('adobe gothic std kalin', 60, True, True)
            info = 'VITÓRIA DO BRASIL!'
            menu = 'MENU'
            restart = 'RESTART'
            mensagem_final = fonte5.render(info, True, (255, 255, 255))
            ret_informacao = mensagem_final.get_rect()
            fim = True
            while fim:
                finalbrasil.draw()
                mensagemcaixa.draw()
                caixamenu.draw()
                caixarestart.draw()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
                    if teclado.key_pressed("ESC"):
                        return
                if Mouse.is_over_object(caixamenu):
                    menu_formatado = fonte5.render(menu, True, (218, 165, 32))
                else:
                    menu_formatado = fonte5.render(menu, True, (255, 255, 255))
                if Mouse.is_over_object(caixarestart):
                    restart_formatado = fonte5.render(restart, True, (218,165,32))
                else:
                    restart_formatado = fonte5.render(restart, True, (255, 255, 255))
                if Mouse.is_button_pressed(1) and clique == 0:
                    if Mouse.is_over_object(caixamenu):
                        return
                    if Mouse.is_over_object(caixarestart):
                        pad1.y = 0
                        pad2.y = 0
                        jogoduo(barulho)
                if clique > 0:
                    clique -= 1
                ret_informacao.center = (largura//2,50)
                tela.blit(mensagem_final,ret_informacao)
                tela.blit(menu_formatado, (200,altura-90))
                tela.blit(restart_formatado, (630, altura-90))
                pygame.display.update()
    
        if pontodir == 5:
            fonte5 = pygame.font.SysFont('adobe gothic std kalin', 60, True, True)
            info = 'VITÓRIA DA ARGENTINA!'
            menu = 'MENU'
            restart = 'RESTART'
            mensagem_final = fonte5.render(info, True, (255, 255, 255))
            ret_informacao = mensagem_final.get_rect()
            fim = True
            while fim:
                finalargentina.draw()
                mensagemcaixa.draw()
                caixamenu.draw()
                caixarestart.draw()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()
                    if teclado.key_pressed("ESC"):
                        return
                if Mouse.is_over_object(caixamenu):
                    menu_formatado = fonte5.render(menu, True, (218, 165, 32))
                else:
                    menu_formatado = fonte5.render(menu, True, (255, 255, 255))
                if Mouse.is_over_object(caixarestart):
                    restart_formatado = fonte5.render(restart, True, (218,165,32))
                else:
                    restart_formatado = fonte5.render(restart, True, (255, 255, 255))
                if Mouse.is_button_pressed(1) and clique == 0:
                    if Mouse.is_over_object(caixamenu):
                        return
                    if Mouse.is_over_object(caixarestart):
                        pad1.y = 0
                        pad2.y = 0
                        jogoduo(barulho)
                if clique > 0:
                    clique -= 1
                ret_informacao.center = (largura // 2, 50)
                tela.blit(mensagem_final, ret_informacao)
                tela.blit(menu_formatado, (200, altura - 90))
                tela.blit(restart_formatado, (630, altura - 90))
                pygame.display.update()

        janela.set_background_color((0, 255, 100))
        maraca.draw()
        bola.draw()
        tela.blit(texto_formatado, (390, 30))
        pad1.draw()
        pad2.draw()
        brasil.draw()
        argentina.draw()
        janela.update()