# Gabriel Maia Alves Araújo - 2022005689
# CMCO05 - INTRODUÇÃO À COMPUTAÇÃO VISUAL - Trabalho 1

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from skimage import io, data
from skimage.transform import rescale, resize, downscale_local_mean

from matplotlib import pyplot as plt

img = io.imread("BD-Imagem/cachorro.jpg", as_gray=True)
rescaled_img = rescale(img, 1.0/4.0, anti_aliasing=True)
resized_img = resize(img, (200, 200))
donwload_img = downscale_local_mean(img, (4,3))
plt.imshow(donwload_img)

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

arestas = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

def Forma():
    glBegin(GL_LINES)
    for aresta in arestas:
        for vertice in aresta:
            glColor3f(1.0, 0.0, 0.0)
            glVertex3fv(vertices[vertice])
    glEnd()

def Ponto():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Forma()
        pygame.display.flip()
        pygame.time.wait(10)

Ponto()

# print('Deseja rotacionar e transladar o cubo [Y/N]? ')
# condicao = input()

# if condicao == 'N' or condicao == 'n':
#     x = 0
#     y = 0
#     angulo = 0
#     Ponto(x, y, angulo)

# if condicao == 'Y' or condicao == 'y':
#     x = 5
#     y = 5
#     angulo = 45
#     Ponto(x, y, angulo)