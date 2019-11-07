import Cells


class Entity():
    def __init__(self):
        self.hitbox = Cells.Cells(1, 1)
        self.live = True
        self.position = Position
        self.speed = 32

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed

    def get_live(self):
        return self.live

    def die(self):
        self.live = False
