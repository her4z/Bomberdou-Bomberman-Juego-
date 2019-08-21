import pygame, sys
from pygame.locals import *

pygame.init()
color = (15, 50, 255)  # Rojo, verde, azul. 0-255
colorDos = pygame.Color(255, 120, 9)
(ancho, alto) = (800, 600)  # Tamaño ventana
ventana = pygame.display.set_mode((ancho, alto))  # regresa una superficie
pygame.draw.line(ventana, colorDos, (100, 80), (780, 90), 10)

print(colorDos.r)
pygame.display.set_caption("Hola")  # Título ventana
pygame.display.flip()
activo = True

# while activo:
#     ventana.fill(colorDos)
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             activo = False
#     pygame.display.update()

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

# class Juego():
#     def __init__(self):
#         pygame.display.flip()

#     def iniciar(self):
#         pygame.init()
    
#     def terminar(self):
#         pygame.quit
#         sys.exit

# class ventana(Juego):
#     def __init____(self):
#         (ancho, alto) = (800, 600)
#         self.pygame.display.set_mode(ancho, alto)
    

