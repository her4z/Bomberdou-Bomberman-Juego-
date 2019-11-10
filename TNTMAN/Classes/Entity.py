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
