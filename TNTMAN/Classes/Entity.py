import Cells


class Entity():

    """Abstract class 'Entity' works so both enemies and player have
       the ability to move, health, life and a defined speed, and code
       can be recicled."""

    def __init__(self):
        self.live = True
        self.hp = 100
        self.position = None
        self.speed = 0.00

    def get_speed(self):  # Getter
        return self.speed

    def set_speed(self, speed):  # Setter
        self.speed = speed

    def get_live(self):  # Getter
        return self.live

    def die(self):  # Can be killed
        self.live = False

    def get_hp(self):  # Getter
        return self.hp

    def set_hp(self, hp):  # Setter
        self.hp = hp

    def is_position_valid(self, direction, objective):
        """ Checks if a particular cell is filled with a block, if it
            is, the player can't move in that direction."""
        new_position = self.TNTMan.get_new_possible_position(direction)
        for i in range(len(self.map_array)):  # Checks full array.
            if self.map_array[i].position == new_position:
                if isinstance(self.map_array[i].content, Blocks.Blocks):
                    return False
        return True
