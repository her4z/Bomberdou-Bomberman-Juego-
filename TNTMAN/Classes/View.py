import pygame
import sys
import os
from pygame.locals import *
import TNTMan as pinguman
import Driver
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
        self.cell_id_dict = None
        self.tntman = None
        self.tntman_sprites = [
                        pygame.image.load(
                            "../src/pinguino/pinguino_right.png"),
                        pygame.image.load(
                            "../src/pinguino/pinguino_left.png"),
                        pygame.image.load(
                            "../src/pinguino/pinguino_upwards.png"),
                        pygame.image.load(
                            "../src/pinguino/pinguino_downwards.png")
                            ]

        def build_map_array_view(self):
            map_array_view = []
            cell_id_dict = {}
            i = -1
            for x in range(0, 26):
                for y in range(0,20):
                    i = i + 1
                    cell_id_dict[x, y] = i
                    map_array_view.append([
                                           (self.map.map_array[i].position)[0] * 32, (self.map.map_array[i].position)[1] *32])
            self.map_array_view = map_array_view
            self.cell_id_dict = cell_id_dict
        build_map_array_view(self)



    def load_background(self, background_img):
        self.background = pygame.image.load(background_img)
        self.screen.blit(self.background, [0, 0])

    def reload_background(self):
        self.screen.blit(self.background, [0, 0])

    def load_sprite_tntman(self, sprite_file):
        self.tntman = pygame.image.load("../src/pinguino/pinguino_right.png")
        self.pos_tntman = self.map.get_position_tntman()
        self.screen.blit(self.tntman, self.pos_tntman)

    def cambiar_sprite_tntman(self, direction):
        if direction == '275':
            self.tntman = self.tntman_sprites[0]
        elif direction == '276':
            self.tntman = self.tntman_sprites[1]
        elif direction == '273':
            self.tntman = self.tntman_sprites[2]
        elif direction == '274':
            self.tntman = self.tntman_sprites[3]

    def reload_tntman(self):
        self.screen.blit(self.tntman, self.search_in_map_array_view(self.map.get_position_tntman()))
    
    def search_in_map_array_view(self, cell):
        cell_id = 0
        cell_id = self.cell_id_dict[cell[0], cell[1]]
        return(self.map_array_view[cell_id])

