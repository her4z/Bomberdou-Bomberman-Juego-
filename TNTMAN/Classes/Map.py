import TNTMan
import View
import sys
import os
import Cells
import Blocks
import Bomb
sys.path.append(os.path.dirname(__file__))


class Map():
    def __init__(self, player_name, dimentions):
        self.name = player_name
        self.dimentions = dimentions
        self.map_array = []
        self.TNTMan = TNTMan.TNTMan(self.name)
        self.Bomb = Bomb.Bomb(None)

        def build_map_array(self):
            map_array = []
            border_list = []
            for column in range(0, 25):
                border_list.append([column, 0])
                border_list.append([column, 18])
            for row in range(1, 18):
                border_list.append([0, row])
                border_list.append([24, row])
            for x in range(0, 25):
                for y in range(0, 19):
                    if [x, y] in border_list:
                        map_array.append(Cells.Cells([x, y], Blocks.Blocks()))
                    elif (x % 2) == 0 and (y % 2) == 0:
                        map_array.append(Cells.Cells([x, y], Blocks.BUnbreakable()))
                        #View.View.load_BUnbreakable_sprite([x, y])
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

    def destroy_bomb(self):
        bomb_position = self.Bomb.get_position()
        self.Bomb.set_position(None)
        self.map_array[bomb_position].content = []

    def is_there_any_bomb(self):
        for i in range(len(self.map_array)):
            if isinstance(self.map_array[i].content, Bomb.Bomb):
                return True
        return False

    def deploy_bomb(self, key):
        if key == 32:
            tntman_pos = self.get_position_tntman()
            for index in range(len(self.map_array)):
                if self.map_array[index].position == tntman_pos:
                    self.map_array[index].content = Bomb.Bomb(tntman_pos)
                    break
