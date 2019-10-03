import pygame
from pygame.locals import *
import TNTMan


class View():
    def __init__(self, dimentions, map):
        pygame.init()
        self.map = map
        self.dimentions = dimentions
        self.background = None
        self.screen = pygame.display.set_mode(dimentions)
        self.tntman = None

    def load_background(self, background_img):
        self.background = pygame.image.load(background_img)
        self.screen.blit(self.background, [0, 0])

    def reload_background(self):
        self.screen.blit(self.background, [0, 0])

    def load_image_tntman(self, sprite, position):
        self.tntman = pygame.image.load(sprite)
        self.pos_tntman = position
        self.screen.blit(self.tntman, self.map.get_position_tntman())

    def reload_tntman(self):
        self.screen.blit(self.tntman, self.map.get_position_tntman())
