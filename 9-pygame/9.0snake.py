#==========================================
#0.importando as coisa
#==========================================
from random import randint
from sys import exit
import pygame
from pygame.locals import *
#==========================================
#1.criando a janela
#==========================================

pygame.init()

LARGURA = 600
ALTURA = 400
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption(' New Lirili Larila Adventures EX Six Seven Deluxe V2+ ')

#==========================================
#2.criando o relogio de fps
#==========================================

relogio = pygame.time.Clock()

#pygame.mixer.music.load('BoxCat_Games_-_08_-_CPU_Talk.ogg.mp3')
#pygame.mixer.music.set_volume(0.3)
#pygame.mixer.music.play(-1)
#com_comida = pygame.mixer.Sound('smw_coin.wav')

#definindo tamanho de blocos e fundo

TAMANHO_GRAMADO=20

COR_FUNDO=('#6CDD20')
COR_GRAMA=('#7EEB26')

#4. esturturando estado inicial cobrinha

inicio = [
    pygame.Rect(x,200,TAMANHO_GRAMADO,TAMANHO_GRAMADO)
    for x in (80,60,40)
]
cobra = inicio.copy()

#5. movimento cobrinha

VELOCIDADEX = TAMANHO_GRAMADO
VELOCIDADEY = 0

comida_x = randint(0,(LARGURA-TAMANHO_GRAMADO) // TAMANHO_GRAMADO) * TAMANHO_GRAMADO
comida_y = randint(0,(ALTURA-TAMANHO_GRAMADO) // TAMANHO_GRAMADO) * TAMANHO_GRAMADO
comida = pygame.Rect(comida_x, comida_y, TAMANHO_GRAMADO, TAMANHO_GRAMADO)

#9.iniciando a pontuação dos games

pontos = 0

fonte = pygame.font.SysFont('Comic Sans MS', 20, bold = True)
# =========================================
#looping
#==========================================
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            rodando = False
        #criando os controles no teclado
        elif evento.type == KEYDOWN:
            if evento.key == K_LEFT and VELOCIDADEX == 0:
                VELOCIDADEX = -TAMANHO_GRAMADO
                VELOCIDADEY = 0

            elif evento.key == K_RIGHT and VELOCIDADEX == 0:
                VELOCIDADEX = TAMANHO_GRAMADO
                VELOCIDADEY = 0

            elif evento.key == K_UP and VELOCIDADEY == 0:
                VELOCIDADEX = 0
                VELOCIDADEY = -TAMANHO_GRAMADO

            elif evento.key == K_DOWN and VELOCIDADEY == 0:
                VELOCIDADEX = 0
                VELOCIDADEY = TAMANHO_GRAMADO

#6. atualizar posiçÃO cobra

    cabeca = pygame.Rect(
         cobra[0].x + VELOCIDADEX,
         cobra[0].y + VELOCIDADEY,
         TAMANHO_GRAMADO,
         TAMANHO_GRAMADO
    )

    cobra.insert(0,cabeca)
    #8.colisão da cobra com a fruta
    if cobra[0].colliderect(comida):
        comida.x = randint(0,(LARGURA-TAMANHO_GRAMADO) // TAMANHO_GRAMADO) * TAMANHO_GRAMADO
        comida.y = randint(0,(ALTURA-TAMANHO_GRAMADO) // TAMANHO_GRAMADO) * TAMANHO_GRAMADO

        pontos += 1#9. soma dos pontos

        #com_comida.play()
    else:
        cobra.pop()
    if(
        cobra[0].x < 0
        or cobra[0].x >= LARGURA
        or cobra[0].y < 0
        or cobra[0].y >= ALTURA
        or any(cobra[0].colliderect(parte) for parte in cobra[1:])
    ):
        cobra = inicio.copy()

        velocidade_x = TAMANHO_GRAMADO
        velocidade_y = 0

        pontos = 0

        comida.x = randint(0,(LARGURA-TAMANHO_GRAMADO) // TAMANHO_GRAMADO) * TAMANHO_GRAMADO
        comida.y = randint(0,(ALTURA-TAMANHO_GRAMADO) // TAMANHO_GRAMADO) * TAMANHO_GRAMADO
        
#pintando tela do jogo
    tela.fill(COR_FUNDO)

#7.desenhando o fundo quadriculado

    for x in range(0, LARGURA, TAMANHO_GRAMADO):
        for y in range(x % 40, ALTURA, 40):
             pygame.draw.rect(tela, COR_GRAMA, (x,y, TAMANHO_GRAMADO, TAMANHO_GRAMADO))


    #agora é fazer acomida da cobra... ohh yes

    pygame.draw.rect(tela,'red',comida,0,6)
#8.estruturar o estado inicial da cobra

    for parte in cobra:
         pygame.draw.rect(tela,'#EE44A1',parte,0,6)
#9.renderizando o placar na tela
    mensagem_placar=f'pontos: {pontos}'
    texto_formatado= fonte.render(mensagem_placar,True, ("#FDF7FA"))
    tela.blit(texto_formatado, (20,20))
#atualizar o game

    pygame.display.flip()

#taxa de x frames
    relogio.tick(10)

pygame.quit()
exit()