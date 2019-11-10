

class Bomb():
    def __init__(self, pos):
        self.position = pos
        self.is_bomb_placed = False

    def get_position(self):
        return self.position

    def set_position(self, pos):
        self.position = pos


