import Cells


class Entity():
    """Abstract class 'Entity' works so both enemies and player have
       the ability to move, health, life and a defined speed, and code
       can be recicled."""
    def __init__():
        self.hitbox = Cells.Cells(1, 1)
        self.live = True
        self.lifes = 0
        self.position = Position
        self.speed = 0.00

    def get_speed():  # Getter
        return self.speed

    def set_speed(speed):  # Setter
        self.speed = speed

    def get_live():  # Getter
        return self.live

    def die():  # Can be killed
        self.live = False

    def get_lifes():  # Getter
        return self.lifes

    def set_lifes(lifes):  # Setter
        self.lifes = lifes
