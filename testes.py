import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from skimage import io

vertices = [
    (-1.0, -1.0,  1.0), ( 1.0, -1.0,  1.0), ( 1.0,  1.0,  1.0), (-1.0,  1.0,  1.0),
    # Face traseira
    ( 1.0, -1.0, -1.0), (-1.0, -1.0, -1.0), (-1.0,  1.0, -1.0), ( 1.0,  1.0, -1.0),
    # Face superior
    (-1.0,  1.0,  1.0), ( 1.0,  1.0,  1.0), ( 1.0,  1.0, -1.0), (-1.0,  1.0, -1.0),
    # Face inferior
    (-1.0, -1.0, -1.0), ( 1.0, -1.0, -1.0), ( 1.0, -1.0,  1.0), (-1.0, -1.0,  1.0),
    # Face direita
    ( 1.0, -1.0,  1.0), ( 1.0, -1.0, -1.0), ( 1.0,  1.0, -1.0), ( 1.0,  1.0,  1.0),
    # Face esquerda
    (-1.0, -1.0, -1.0), (-1.0, -1.0,  1.0), (-1.0,  1.0,  1.0), (-1.0,  1.0, -1.0),
]

texture_coords = [
    (0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0),
    # Face traseira
    (0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0),
    # Face superior
    (0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0),
    # Face inferior
    (0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0),
    # Face direita
    (0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0),
    # Face esquerda
    (0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0),
]


def load_texture():
    textureSurface = pygame.image.load('BD-Imagem/cachorro.jpg')
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texid

def Cubo(texture_id):
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glBegin(GL_QUADS)
    for tex_coord, vertex in zip(texture_coords, vertices):
        glTexCoord2f(*tex_coord)
        glVertex3f(vertex[0] * 1.0, vertex[1] * 1.0, vertex[2] * 1.0)
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    glEnable(GL_TEXTURE_2D)
    texture_id = load_texture()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cubo(texture_id)
        pygame.display.flip()
        pygame.time.wait(10)

main()
