import pygame
from pygame.locals import *
import bomberman


class View():
    def __init__(self, dimentions, map):
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
