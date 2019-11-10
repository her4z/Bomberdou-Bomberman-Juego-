import pygame  # Import pygame module.
import os      # Import sys and os for python to understand the local
import sys     # directory.
from pygame.locals import *
import TNTMan  # Import 'TNTMan.py' file.
import Driver  # Import 'Driver.py' file.
sys.path.append(os.path.dirname(__file__))


class View():

    """ View creates everything the user must see to play the game and
    controls every graphic change the game window presents."""

    def __init__(self, dimentions, map):
        pygame.init()  # Initialize pygame .
        self.dimentions = dimentions  # Saves received dimentions in attribute.
        self.background = None  # Defines background attribute.
        self.screen = pygame.display.set_mode(self.dimentions)  # Set screen as
        # pygame display method with dimentions attribute.
        self.caption = pygame.display.set_caption("TNTMan")  # Set caption
        # attribute as pygame display caption.
        pygame.display.flip()  # Refresh pygame display.
        self.map = map  # Set map attribute as map received.
        self.map_array_view = None
        # Prepares the array that contains the cells to graphic using later on.
        self.cell_id_dict = None
        # Prepare the dictionary that later will give
        # each cell a particular ID to be found if needed.
        self.tntman = None
        self.bomb_sprite = pygame.image.load("../src/keybomb.png")
        self.load_background('../src/background.png')  # Sets background image
        self.BUnbreakable_sprite = pygame.image.load(  # Loads unbreakable
                                                       # blocks image.
                                   "../src/bUnbreakable32x32.png")
        self.BBreakable_sprite = pygame.image.load("../src/bBreakable32x32.png")
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

        self.load_sprite_tntman("../src/pinguino/pinguino_right.png")  # Loads
        # the tntman sprite for the first time.

        def build_map_array_view(self):

            """ Building the map array on the view file helps us locate
                graphically our player, the bomb and enemies, so we can
                put their sprites where they are according to the Map."""

            map_array_view = []
            # Creates empty list, to be filled with cells x and y locations in
            # pixels.
            cell_id_dict = {}  # Creates empty dictionary, each cell will have
            # an i value.
            i = -1  # Defines i var with a value of -1 to fits properly into de
            # For statement.
            size_value = 32  # Pixel dimentions of cells.
            x_cells = 25  # Defining the cell array
            y_cells = 19  # size.

            for x in range(x_cells):  # Building array with [x_cells, y_cells]
                for y in range(y_cells):  # dimention.
                    """ The array starts to get filled up, adding one
                        cell, using the already created array on Map.
                        To do this, it uses the value of 'i' to grab
                        the value in that index and then it multiplies
                        for the size value of each cell, which is 32."""
                    i = i + 1  # Plus one every time.
                    cell_id_dict[x, y] = i  # For ex.: cell_id_dict[0, 1] = 1

                    # Saves in a list the cell position
                    # but in pixels instead.
                    map_array_view.append([(self.map.map_array[i].position)[0]
                                            * size_value, (self.map.map_array[i].\
                                            position)[1] * size_value])

            self.map_array_view = map_array_view  # Saves the array and the
            self.cell_id_dict = cell_id_dict      # dictionary of cells into
                                                  # attributes.

        build_map_array_view(self)  # Build the visual version
        # of the map array.

    def load_blocks(self):  # Loads unbreakable and breakable blocks

        """ Using a list made on the map class, View fullfils not
            logically but graphically, allowing the player to see
            the walls they could collision with."""

        B_unbreakable_list = self.map.get_B_unbreakable_list()  # Get the logical list of unbreakable blocks.
        for cell in range(len(B_unbreakable_list)):  # Iterate over unbreakable blocks list.
            cell_block = B_unbreakable_list[cell]  # Saves the block cell.
            cell_px = self.search_in_map_array_view(cell_block)  # Returns the pixel convertion of the cell and saves it.
            self.screen.blit(self.BUnbreakable_sprite, cell_px)  # Loads into buffer the image and position of the block.

        B_breakable_list = self.map.get_B_breakable_list()  # Get the logical list of breakable blocks.
        for cell in range(len(B_breakable_list)):  # Iterate over breakable blocks list.
            cell_block = B_breakable_list[cell]  # Saves the block cell.
            cell_px = self.search_in_map_array_view(cell_block)  # Returns the pixel convertion of the cell and saves it.
            self.screen.blit(self.BBreakable_sprite, cell_px)  # Loads into buffer the image and position of the block.

    def load_background(self, background_img):

        """ Loads the background image for the first time. """

        self.background = pygame.image.load(background_img)  # Loads background image with the path received.
        self.screen.blit(self.background, [0, 0])  # Loads into buffer the background image.

    def reload_background(self):  # Reloads the background image.
        self.screen.blit(self.background, [0, 0])  # Loads into buffer the background

    def load_sprite_tntman(self, sprite_path):  # Loads the tntman image.

        """ Loads the character image for the first time. """

        self.tntman = pygame.image.load(sprite_path)  # Loads the tntman image with the path received.
        pos_tntman = self.map.get_position_tntman()  # Gets the tntman position in the map and saves it.
        self.screen.blit(self.tntman, pos_tntman)  # Loads into buffer the tntman image and its position.

    def load_sprite_bomb(self, key):  # Loads the bomb image.
        if key == 32:  # If key it's spacebar:
            pos_bomb = self.map.get_position_bomb()  # Get the bomb position and saves it.
            pos_bomb_pixels = self.search_in_map_array_view(pos_bomb)  #  Get the pixel's position of the bomb and saves it.
            self.screen.blit(self.bomb_sprite, pos_bomb_pixels)  # Loads into buffer the bomb image and its position.

    def reload_bomb(self):  # Reloads the bomb image on position.
        pos_bomb = self.map.get_position_bomb()  # Get the bomb position and saves it.
        pos_bomb_pixels = self.search_in_map_array_view(pos_bomb)  # Get the pixel's position of the bomb and saves it.
        self.screen.blit(self.bomb_sprite, pos_bomb_pixels)  # Loads into buffer the bomb image and its position.

    def reload_tntman(self):  # Reloads the character's sprites.
        self.screen.blit(self.tntman, self.search_in_map_array_view  # Loads into buffer
                         (self.map.get_position_tntman()))  # the tntman image and its position.

    def change_tntman_sprite(self, direction):  # Change the tntman image
        # regard of the direction received.

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

    def search_in_map_array_view(self, cell):  # Converts the cell position
        # given into pixels parameters.

        """ When called, this method uses the id dictionary to search
            for a cell, using a specific parameter."""

        cell_id = 0  # Represents the cell's index.
        cell_id = self.cell_id_dict[cell[0], cell[1]]  # Search for the
        # cell ID which represents the cell position given and returns it.
        return(self.map_array_view[cell_id])  # Returns the pixel's position
        # of the cell.
