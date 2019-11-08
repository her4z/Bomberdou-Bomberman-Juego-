import pygame
import sys
import os
from pygame.locals import *
import TNTMan as pinguman
import Driver
sys.path.append(os.path.dirname(__file__))


class View():
    """ View creates everything the user must see to play the game and
    controls every graphic change the game window presents."""
    def __init__(self, dimentions, elmapaquerecibecomoparametro):
        pygame.init()
        self.dimentions = dimentions  # Gotten from Driver dimentions.
        self.background = None
        self.screen = pygame.display.set_mode(self.dimentions)  # Sets screen
        self.caption = pygame.display.set_caption("TNTMan")
        pygame.display.flip()
        self.map = elmapaquerecibecomoparametro
        self.map_array_view = None
        # Prepares the array that contains the cells to graphic using later on.
        self.cell_id_dict = None
        # Gives each cell a particular ID to be found if needed
        self.tntman = None
        self.bomb_sprite = pygame.image.load("../src/keybomb.png")
        self.load_background('../src/background.png')  # Sets background image
        self.load_sprite_tntman("")  # Sets an empty sprite to be changed
        self.BUnbreakable_sprite = pygame.image.load(  # Loads unbreakable
                                                       # blocks image.
                                   "../src/bUnbreakable32x32.png")
        self.tntman_sprites = [  # Loads every pinguino sprite, so we
                                 # can change it when the direction
                                 # changes.
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
            """ Building the map array on the view file helps us locate
                graphically our player, the bomb and enemies, so we can
                put their sprites where they are according to the Map."""
            map_array_view = []  
            # Creates empty list, to be filled with cells x and y locations
            cell_id_dict = {}  # Creates empty dictionary, each cell will have
                               # an i value
            i = -1
            size_value = 32
            x_cells = 25
            y_cells = 19
            for x in range(x_cells):
                for y in range(y_cells):
                    """ The array starts to get filled up, adding one
                        cell, using the already created array on Map.
                        To do this, it uses the value of 'i' to grab
                        the value in that index and then it multiplies
                        for the size value of each cell, which is 32."""
                    i = i + 1
                    cell_id_dict[x, y] = i # For ex.: cell_id_dict[0, 1] = 1
                    map_array_view.append([(self.map.map_array[i].position)[0]
                                            * size_value, (self.map.map_array[i].\
                                            position)[1] * size_value])
            self.map_array_view = map_array_view
            self.cell_id_dict = cell_id_dict

        def load_B_unbreakable(self):  # Loads unbreakable blocks
            """ Using a list made on the map class, View fullfils not
                logically but graphically, allowing the player to see
                the walls they could collision with."""
            B_unbreakable_list = self.map.get_B_unbreakable_list()
            for cell in range(len(B_unbreakable_list)):
                cell_block = B_unbreakable_list[cell]
                cell_px = self.search_in_map_array_view(cell_block)
                self.screen.blit(self.BUnbreakable_sprite, cell_px)

        build_map_array_view(self)
        load_B_unbreakable(self)

    def load_B_unbreakable(self):
        B_unbreakable_list = self.map.get_B_unbreakable_list()
        for cell in range(len(B_unbreakable_list)):
            cell_block = B_unbreakable_list[cell]
            cell_px = self.search_in_map_array_view(cell_block)
            self.screen.blit(self.BUnbreakable_sprite, cell_px)

    def load_background(self, background_img):  
        """ Loads the background image for the first time. """
        self.background = pygame.image.load(background_img)
        self.screen.blit(self.background, [0, 0])

    def reload_background(self):  # Reloads the background image.
        self.screen.blit(self.background, [0, 0])

    def load_sprite_tntman(self, sprite_file):
        """ Loads the character image for the first time. """
        self.tntman = pygame.image.load("../src/pinguino/pinguino_right.png")
        pos_tntman = self.map.get_position_tntman()
        self.screen.blit(self.tntman, pos_tntman)

    def load_sprite_bomb(self, key):  # Loads sprite image
        if key == 32:
            pos_tntman = self.map.get_position_tntman()
            pos_tntman_pixels = self.search_in_map_array_view(pos_tntman)
            self.screen.blit(self.bomb_sprite, pos_tntman_pixels)

    def reload_bomb(self):  # Reloads sprite image on position
        pos_tntman = self.map.get_position_tntman()
        pos_tntman_pixels = self.search_in_map_array_view(pos_tntman)
        self.screen.blit(self.bomb_sprite, pos_tntman_pixels)

    def reload_tntman(self):  # Reloads the character's sprites.
        self.screen.blit(self.tntman, self.search_in_map_array_view
                         (self.map.get_position_tntman()))

    def change_tntman_sprite(self, direction):
        """According to which key is pressed, the Driver sends a string
           that contains the number associated to the key pressed.
           Those are used to select an image from the
           'self.tntman_sprites' attribute."""
        if direction == '275':  # Right
            self.tntman = self.tntman_sprites[0] 
        elif direction == '276':  # Left
            self.tntman = self.tntman_sprites[1]
        elif direction == '273':  # Upwards
            self.tntman = self.tntman_sprites[2]
        elif direction == '274':  # Downwards
            self.tntman = self.tntman_sprites[3]

    def search_in_map_array_view(self, cell):
        """ When called, this method uses the id dictionary to search
            for a cell, using a specific parameter."""
        cell_id = 0
        cell_id = self.cell_id_dict[cell[0], cell[1]]
        return(self.map_array_view[cell_id])
