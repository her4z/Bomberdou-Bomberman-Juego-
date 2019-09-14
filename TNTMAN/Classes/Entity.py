class Entity():
    def __init__ (self):
        Entity.__init__(self)
        self.hitbox = Cells[2]
        self.live = True
        self.lifes = 0
        self.position = Position
        self.speed = 0.00

    def getSpeed():
        return self.speed
    def setSpeed(speed):
        self.speed = speed
    def getLive():
        return self.live
    def die():
        self.live = False
    def getLifes():
        return self.lifes
    def setLifes(lifes):
        self.lifes = lifes


    