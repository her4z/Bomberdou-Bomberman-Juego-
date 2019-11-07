import TNTMan
import View
import sys
import os
import Cells
import Blocks
sys.path.append(os.path.dirname(__file__))


class Map():
    def __init__(self, player_name, dimentions):
        self.name = player_name
        self.dimentions = dimentions
        self.map_array = []
        self.TNTMan = TNTMan.TNTMan(self.name)

        def build_map_array(self):
            map_array = []
            border_list = []
            for a in range(0, 25):
                border_list.append([a, 0])
                border_list.append([a, 18])
            for b in range(1, 18):
                border_list.append([0, b])
                border_list.append([24, b])
            for x in range(0, 25):
                for y in range(0, 19):
                    if [x, y] in border_list:
                        map_array.append(Cells.Cells([x, y], Blocks.Blocks()))
                    else:
                        map_array.append(Cells.Cells([x, y], None))

            self.map_array = map_array
        build_map_array(self)

    def is_position_valid(self, direction):
        new_position = self.TNTMan.get_new_possible_position(direction)
        for i in range(len(self.map_array)):
            if self.map_array[i].position == new_position:
                if isinstance(self.map_array[i].content, Blocks.Blocks):
                    raise KeyError

    def get_position_tntman(self):
        return self.TNTMan.get_position()

    def move_tm(self, direction):

        self.TNTMan.move_to(direction, 1)
