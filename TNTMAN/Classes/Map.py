import Driver
import TNTMan

class Map():
    def __init__(self, player_name, dimentions):
        self.name = player_name
        self.dimentions = dimentions
        self.TNTMan = TNTMan.TNTMan(self.name)

    def is_position_valid(self, moveTo):
        new_position = self.bomberman.get_new_movable_position(moveTo)


        