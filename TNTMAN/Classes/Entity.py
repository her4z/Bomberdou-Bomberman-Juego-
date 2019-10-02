class Entity():
    def __init__ (self):
        self.hitbox = Cells[2]
        self.live = True
        self.lifes = 0
        self.position = Position
        self.speed = 0.00

    def get_speed():
        return self.speed
    def set_speed(speed):
        self.speed = speed
    def get_live():
        return self.live
    def die():
        self.live = False
    def get_lifes():
        return self.lifes
    def set_lifes(lifes):
        self.lifes = lifes


    