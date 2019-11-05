import pygame
import sys
import os
from pygame.locals import *
import TNTMan as pinguman
import Driver
import Map
sys.path.append(os.path.dirname(__file__))


class View():
    def __init__(self, dimentions, elmapaquerecibecomoparametro):
        pygame.init()
        self.dimentions = dimentions
        self.background = None
        self.screen = pygame.display.set_mode(self.dimentions)
        self.caption = pygame.display.set_caption("TNTMan")
        pygame.display.flip()
        self.map = elmapaquerecibecomoparametro
        self.map_array_view = None
        self.tntman = None
        self.tntman_sprites = [
                            pygame.image.load("../src/pinguino/pinguino1.png"),
                            pygame.image.load("../src/pinguino/pinguino2.png"),
                            pygame.image.load("../src/pinguino/pinguino3.png"),
                            pygame.image.load("../src/pinguino/pinguino4.png")
                            ]

        def build_map_array_view(self):
            map_array_view = []
            i = -1
            for x in range(0, 26):
                for y in range(0,20):
                    i = i + 1
                    map_array_view.append([(self.map[i].position)[0] * 32, (self.map[i].position)[1] *32])
            self.map_array_view = map_array_view
        build_map_array_view(self)



    def load_background(self, background_img):
        self.background = pygame.image.load(background_img)
        self.screen.blit(self.background, [0, 0])

    def reload_background(self):
        self.screen.blit(self.background, [0, 0])

    def load_sprite_tntman(self, sprite_file):
        self.tntman = pygame.image.load("../src/pinguino/pinguino1.png")
        self.pos_tntman = self.map.get_position_tntman()
        self.screen.blit(self.tntman, self.pos_tntman)

    def cambiar_sprite_tntman(self, direction):
        if direction == '275':
            self.tntman = self.tntman_sprites[0]
        elif direction == '276':
            self.tntman = self.tntman_sprites[2]
        elif direction == '273':
            self.tntman = self.tntman_sprites[3]

    def reload_tntman(self):
        self.screen.blit(self.tntman, self.map.get_position_tntman())
