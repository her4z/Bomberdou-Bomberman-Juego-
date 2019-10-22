import pygame
import sys
from pygame.locals import *
import TNTMan
import Driver
import Map


class View():
    def __init__(self, dimensiones, elmapaquerecibecomoparametro):
        pygame.init()
        # self.map = map
        self.dimentions = dimensiones
        self.background = None
        self.screen = pygame.display.set_mode(self.dimentions)
        self.caption = pygame.display.set_caption("TNTMan")
        pygame.display.flip()
        self.map = elmapaquerecibecomoparametro
        self.tntman = None

    def load_background(self, background_img):
        self.background = pygame.image.load(background_img)
        self.screen.blit(self.background, [0, 0])

    def reload_background(self):
        self.screen.blit(self.background, [0, 0])

    def load_image_tntman(self, ruta_sprite):
        self.tntman = pygame.image.load(ruta_sprite)
        self.pos_tntman = self.map.get_position_tntman()
        self.screen.blit(self.tntman, self.pos_tntman)

    def reload_tntman(self):
        self.screen.blit(self.tntman, self.map.get_position_tntman())