import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from skimage import io

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

faces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
    )

# Coordenadas de textura para cada vértice
texture_coords = (
    (0, 0),
    (1, 0),
    (1, 1),
    (0, 1)
    )

def load_texture(image_path):
    image = io.imread(image_path)
    image = pygame.image.frombuffer(image.tobytes(), image.shape[1::-1], "RGB")
    texture_data = pygame.image.tostring(image, "RGB", 1)

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.get_width(), image.get_height(), 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)
    return texture_id

def Forma():
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glBegin(GL_QUADS)
    for face in faces:
        for i, vertex in enumerate(face):
            glTexCoord2f(texture_coords[i][0], texture_coords[i][1])
            glVertex3fv(vertices[vertex])
    glEnd()

def Ponto():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    glEnable(GL_TEXTURE_2D)
    global texture_id
    texture_id = load_texture('BD-Imagem/cachorro.jpg')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Forma()
        pygame.display.flip()
        pygame.time.wait(10)

Ponto()
