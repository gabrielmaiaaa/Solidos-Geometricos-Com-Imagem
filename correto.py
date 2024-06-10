import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from skimage import io

# Inicializar Pygame e configurar a tela
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Função para carregar uma imagem e convertê-la em textura
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

# Carregar a textura
texture_id = load_texture('BD-Imagem/cachorro.jpg')

# Função para desenhar o cubo
def draw_cube():
    glBegin(GL_QUADS)
    
    # Frente
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)
    glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)
    glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0,  1.0)
    glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0,  1.0)
    
    # Traseira
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, -1.0)
    glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0, -1.0)
    
    # Superior
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0,  1.0, -1.0)
    glTexCoord2f(1.0, 0.0); glVertex3f( 1.0,  1.0, -1.0)
    glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0,  1.0)
    glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0,  1.0)
    
    # Inferior
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1.0); glVertex3f( 1.0, -1.0,  1.0)
    glTexCoord2f(0.0, 1.0); glVertex3f(-1.0, -1.0,  1.0)
    
    # Direita
    glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 0.0); glVertex3f( 1.0,  1.0, -1.0)
    glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0,  1.0)
    glTexCoord2f(0.0, 1.0); glVertex3f( 1.0, -1.0,  1.0)
    
    # Esquerda
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 0.0); glVertex3f(-1.0,  1.0, -1.0)
    glTexCoord2f(1.0, 1.0); glVertex3f(-1.0,  1.0,  1.0)
    glTexCoord2f(0.0, 1.0); glVertex3f(-1.0, -1.0,  1.0)
    
    glEnd()

# Habilitar texturas 2D
glEnable(GL_TEXTURE_2D)
glBindTexture(GL_TEXTURE_2D, texture_id)

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    glRotatef(1, 3, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_cube()
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
