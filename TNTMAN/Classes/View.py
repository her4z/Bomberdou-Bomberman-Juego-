import pygame
import sys
from pygame.locals import *
import TNTMan
import Driver
import Map


class View():
    def __init__(self):
        pygame.init()
        # self.map = map
        self.dimentions = (1024, 480)
        self.background = None
        self.screen = pygame.display.set_mode(self.dimentions)
        self.caption = pygame.display.set_caption("TNTMan")
        pygame.display.flip()
        self.tntman = None
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

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

laseñoravista = View()