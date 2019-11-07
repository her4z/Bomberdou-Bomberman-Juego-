import TNTMan
import View
import sys
import os
import Cells
import Blocks
sys.path.append(os.path.dirname(__file__))


class Map():
    """ Map works as an admin inside the game, checking cells array and
       character position."""
    def __init__(self, dimentions):
        self.dimentions = dimentions  # Gotten from Driver. 
        self.map_array = []  # Creates empty cell array.
        self.TNTMan = TNTMan.TNTMan()  # creates playable character.

        def build_map_array(self):
            """ Bulding this array of cells helps programming movement
                and space indications."""
            map_array = []
            border_list = []
            for a in range(0, 25):  # Adds top and bottom borders.
                border_list.append([a, 0])
                border_list.append([a, 18])
            for b in range(1, 18): # Adds left and right borders.
                border_list.append([0, b])
                border_list.append([24, b])
            for x in range(0, 25): 
                for y in range(0, 19):
                    if [x, y] in border_list: 
                        """ 
                            Creates array based on x and y values in
                            for and fills them with solid blocks if the
                            cells are inside of the 'border_list' list,
                            making them incapable of being stepped on.
                        """
                        map_array.append(Cells.Cells([x, y], Blocks.Blocks()))
                    else:
                        map_array.append(Cells.Cells([x, y], None))

            self.map_array = map_array
        build_map_array(self)

    def is_position_valid(self, direction):
        """ Checks if a particular cell is filled with a block, if it
            is, the player can't move in that direction."""
        new_position = self.TNTMan.get_new_possible_position(direction)
        for i in range(len(self.map_array)): # Checks full array.
            if self.map_array[i].position == new_position:
                if isinstance(self.map_array[i].content, Blocks.Blocks):
                    raise KeyError 

    def get_position_tntman(self):  # Getter.
        return self.TNTMan.get_position()

    def move_tm(self, direction):  # Calls TNTMan to move character.
        self.TNTMan.move_to(direction, 1)
