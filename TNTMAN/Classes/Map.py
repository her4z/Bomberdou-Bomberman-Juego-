import TNTMan
import View
import sys
import os
import Cells
import Blocks
import Bomb
sys.path.append(os.path.dirname(__file__))


class Map():
    """ Map works as an admin inside the game, checking cells array and
       character position."""
    def __init__(self, dimentions):
        self.dimentions = dimentions  # Gotten from Driver.
        self.map_array = []  # Creates empty cell array.
        self.TNTMan = TNTMan.TNTMan()  # creates playable character.
        self.Bomb = Bomb.Bomb(None)

        def build_map_array(self):
            """ Bulding this array of cells helps programming movement
                and space indications."""
            map_array = []
            border_list = []
            B_unbreakable_list = []
            for column in range(0, 25):  # Adds top and bottom borders.
                border_list.append([column, 0])
                border_list.append([column, 18])
            for row in range(1, 18):  # Adds left and right borders.
                border_list.append([0, row])
                border_list.append([24, row])
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
                    elif (x % 2) == 0 and (y % 2) == 0:
                        map_array.append(Cells.Cells([x, y],
                                         Blocks.B_unbreakable()))
                        B_unbreakable_list.append([x, y])
                    else:
                        map_array.append(Cells.Cells([x, y], None))

            self.map_array = map_array
            self.B_unbreakable_list = B_unbreakable_list
        build_map_array(self)

    def get_B_unbreakable_list(self):  # Getter
        return self.B_unbreakable_list

    def is_position_valid(self, direction): 
        """ Checks if a particular cell is filled with a block, if it
            is, the player can't move in that direction."""
        new_position = self.TNTMan.get_new_possible_position(direction)
        for i in range(len(self.map_array)):  # Checks full array.
            if self.map_array[i].position == new_position:
                if isinstance(self.map_array[i].content, Blocks.Blocks):
                    raise KeyError

    def get_position_tntman(self):  # Getter.
        return self.TNTMan.get_position()

    def move_tm(self, direction):  # Calls TNTMan to move character.
        self.TNTMan.move_to(direction, 1)

    def destroy_bomb(self): 
        bomb_position = self.Bomb.get_position()
        self.Bomb.set_position(None)
        self.map_array[bomb_position].content = []

    def is_there_any_bomb(self):
        for cell in range(len(self.map_array)):
            if isinstance(self.map_array[cell].content, Bomb.Bomb):
                return True
        else:
            return False

    def get_position_bomb(self):
        for cell in range(len(self.map_array)):
            if isinstance(self.map_array[cell].content, Bomb.Bomb):
                return self.map_array[cell].position

    def is_bomb_deployed(self):
        return self.TNTMan.get_bomb_deployed()

    def deploy_bomb(self, key):
        if key == 32:
            if self.is_there_any_bomb() is False:
                #self.TNTMan.deploy_bomb()
                tntman_pos = self.get_position_tntman()
                for index in range(len(self.map_array)):
                    if self.map_array[index].position == tntman_pos:
                        self.map_array[index].content = Bomb.Bomb(tntman_pos)
                        break
