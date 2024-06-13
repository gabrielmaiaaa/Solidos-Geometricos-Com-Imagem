# Bibliotecas
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Variáveis do cubo
vertices = [
    (-1.0, -1.0,  1.0), ( 1.0, -1.0,  1.0), ( 1.0,  1.0,  1.0), (-1.0,  1.0,  1.0),
    ( 1.0, -1.0, -1.0), (-1.0, -1.0, -1.0), (-1.0,  1.0, -1.0), ( 1.0,  1.0, -1.0),
    (-1.0,  1.0,  1.0), ( 1.0,  1.0,  1.0), ( 1.0,  1.0, -1.0), (-1.0,  1.0, -1.0),
    (-1.0, -1.0, -1.0), ( 1.0, -1.0, -1.0), ( 1.0, -1.0,  1.0), (-1.0, -1.0,  1.0),
    ( 1.0, -1.0,  1.0), ( 1.0, -1.0, -1.0), ( 1.0,  1.0, -1.0), ( 1.0,  1.0,  1.0),
    (-1.0, -1.0, -1.0), (-1.0, -1.0,  1.0), (-1.0,  1.0,  1.0), (-1.0,  1.0, -1.0),
]

texture_coords = [
    (0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0),
    (0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0),
    (0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0),
    (0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0),
    (0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0),
    (0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0),
]

# Função que gera uma textura a partir de uma imagem
def load_texture():
    textureSurface = pygame.image.load('BD-Imagem/cachorro.jpg')
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()
    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    return texid

# Função que gera o cubo com a textura colocada em sua devida face
def Cubo(texture_id, escala):
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glBegin(GL_QUADS)
    for tex_coord, vertex in zip(texture_coords, vertices):
        glTexCoord2f(*tex_coord)
        glVertex3f(vertex[0] * escala, vertex[1] * escala, vertex[2] * escala)
    glEnd()

# Função principal que gera a tela
def main():
    pygame.init()
    #Variável reponsável pela escala
    escala = 1
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
    texture_id = load_texture()

    # Cria um loop que atualiza o estado do jogo
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # Tratamento de INPUTs
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    escala += 0.1
                elif event.key == pygame.K_e:
                    escala -= 0.1
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
                    moveX += 0.01
                elif event.key == pygame.K_LEFT:
                    moveX -= 0.01
                elif event.key == pygame.K_UP:
                    moveY += 0.01
                elif event.key == pygame.K_DOWN:
                    moveY -= 0.01
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
        glTranslatef(moveX, moveY, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cubo(texture_id, escala)
        pygame.display.flip()
        pygame.time.wait(10)

# Chama a função main
main()
