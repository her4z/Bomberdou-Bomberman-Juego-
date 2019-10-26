import TNTMan
import View
import sys, os
sys.path.append(os.path.dirname(__file__))

class Map():
    def __init__(self, player_name, dimentions):
        self.name = player_name
        self.dimentions = dimentions
        self.TNTMan = TNTMan.TNTMan(self.name)
        self.view = View.View(self.dimentions, self.name)

    def is_position_valid(self, direction):
        new_position = self.TNTMan.get_new_movable_position(direction)

    def get_position_tntman(self):
        return self.TNTMan.get_position()

    def move_tm(self, direction):
        self.TNTMan.move_to(direction, 1)
    
           