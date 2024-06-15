# Bibliotecas importadas
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from skimage import io

# Variáveis dos vértices do cubo
vertices = [
    (-1.0, -1.0,  1.0), ( 1.0, -1.0,  1.0), ( 1.0,  1.0,  1.0), (-1.0,  1.0,  1.0),
    ( 1.0, -1.0, -1.0), (-1.0, -1.0, -1.0), (-1.0,  1.0, -1.0), ( 1.0,  1.0, -1.0),
    (-1.0,  1.0,  1.0), ( 1.0,  1.0,  1.0), ( 1.0,  1.0, -1.0), (-1.0,  1.0, -1.0),
    (-1.0, -1.0, -1.0), ( 1.0, -1.0, -1.0), ( 1.0, -1.0,  1.0), (-1.0, -1.0,  1.0),
    ( 1.0, -1.0,  1.0), ( 1.0, -1.0, -1.0), ( 1.0,  1.0, -1.0), ( 1.0,  1.0,  1.0),
    (-1.0, -1.0, -1.0), (-1.0, -1.0,  1.0), (-1.0,  1.0,  1.0), (-1.0,  1.0, -1.0),
]

# Variáveis da coordenada da textura
coordenadas_textura = [
    (0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0),
    (0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0),
    (0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0),
    (0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0),
    (0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0),
    (0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0),
]

# Função que gera uma textura a partir de uma imagem
def Textura():
    # Carregamos a imagem na nossa váriavel
    imagem = pygame.image.load('BD-Imagem/dogo.jpeg')
    # Transformamos a nossa imagem numa string para poder tratar ela
    textura = pygame.image.tostring(imagem, "RGBA", 1)
    # Variavéis das dimensão da nossa imagem
    width = imagem.get_width()
    height = imagem.get_height()
    # habilita a textura 2D no OpenGL
    glEnable(GL_TEXTURE_2D)
    # Gera a textura e liga a textura para q possamos trabalhar nela
    texid = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texid)
    # comando que define a imagem da textura no OpenGL.
    # que recebe algumas variáveis como tipo de textura, nível de detalhe, formato interno,
    # largura, altura, borda, formato da imagem, tipo de dados e os dados da imagem em si.
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textura)
    # São comandos que configuram os parâmetros de empacotamento e filtragem da textura
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    # Aqui faz a filtragem usar o pixel mais próximo 
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    return texid

# Função que gera o cubo com a textura colocada em sua devida face
def Cubo(texture_id, escalaX, escalaY, escalaZ):
    # Liga a textura para que ela possa ser usado ao desenhar o cubo
    glBindTexture(GL_TEXTURE_2D, texture_id)
    # inicia a definição de um conjunto de quadriláteros
    glBegin(GL_QUADS)
    # loop que desenha as faces do cubo com a textura
    # O loop intera sobre os pares de coordenadas da textura e do vertice do cubo. 
    # Fazendo uma associação de cada vértice com uma coordenada da textura
    for tex_coord, vertex in zip(coordenadas_textura, vertices): 
        glTexCoord2f(*tex_coord)
        glVertex3f(vertex[0] * escalaX, vertex[1] * escalaY, vertex[2] * escalaZ)
    glEnd()

# Função principal que gera a tela
def main():
    pygame.init()
    #Variável reponsável pela escala
    escalaX = 1
    escalaY = 1
    escalaZ = 1
    #Variáveis reponsáveis pela rotação
    speed = 0
    x = 0
    y = 0
    z = 0
    #Variáveis reponsáveis pela translação
    moveX = 0
    moveY = 0
    # Gera tela
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    glEnable(GL_TEXTURE_2D)
    texture_id = Textura()

    # Cria um loop que atualiza o estado do jogo
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # Tratamento de INPUTs
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    escalaX += 0.1
                if event.key == pygame.K_w:
                    escalaY += 0.1
                elif event.key == pygame.K_e:
                    escalaZ += 0.1
                if event.key == pygame.K_t:
                    escalaX -= 0.1
                if event.key == pygame.K_y:
                    escalaY -= 0.1
                elif event.key == pygame.K_u:
                    escalaZ -= 0.1
                elif event.key == pygame.K_a:
                    x += 0.5
                    speed=1
                elif event.key == pygame.K_s:
                    y += 0.5
                    speed=1
                elif event.key == pygame.K_d:
                    z += 0.5
                    speed=1
                elif event.key == pygame.K_RIGHT:
                    moveX = 0.1
                    moveY = 0
                    glTranslatef(moveX, moveY, 0)
                elif event.key == pygame.K_LEFT:
                    moveX = -0.1
                    moveY = 0
                    glTranslatef(moveX, moveY, 0)
                elif event.key == pygame.K_UP:
                    moveX = 0
                    moveY = 0.1
                    glTranslatef(moveX, moveY, 0)
                elif event.key == pygame.K_DOWN:
                    moveX = 0
                    moveY = -0.1
                    glTranslatef(moveX, moveY, 0)
                elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    x = 0
                    y = 0
                    z = 0
                    moveX = 0
                    moveY = 0
                    speed = 0
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        # Atualiza o CUBO
        glRotatef(speed, x, y, z)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cubo(texture_id, escalaX, escalaY, escalaZ)
        pygame.display.flip()
        pygame.time.wait(10)

# Chama a função main
main()
