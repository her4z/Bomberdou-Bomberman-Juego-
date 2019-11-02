import TNTMan
import View
import sys
import os
import Cells
sys.path.append(os.path.dirname(__file__))


class Map():
    def __init__(self, player_name, dimentions):
        self.name = player_name
        self.dimentions = dimentions
        self.TNTMan = TNTMan.TNTMan(self.name)
        self.view = View.View(self.dimentions, self.name)
        self.map = self.build_map(32)
        self.cell = Cells.Cells(32)

    def is_position_valid(self, direction):
        new_position = self.TNTMan.get_new_possible_position(direction)
        xpos = new_position[0]
        ypos = new_position[1] 
        print("next_pos", new_position)
        if(xpos > 32 and xpos < 768 and ypos > 30 and ypos < 576):
            self.move_tm(direction)
        else:
            pass

    def get_position_tntman(self):
        return self.TNTMan.get_position()

    def move_tm(self, direction):
        self.TNTMan.move_to(direction, 1)
    
    def build_map(self, dimentions):
        map_list = []
        for y_rows in range(18):  # 0 a 18 filas (19)
            for x_columns in range(24):  # 0 a 24 filas (25)
                # cell = Cells(y_rows, x_columns)
                # map_list.append(Cells(y_rows, x_columns))
                pass
            print("map_list", map_list)
