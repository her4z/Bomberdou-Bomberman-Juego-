class Bomb():
    """ Bomb functionality bases on the idea of erasing every entity or
        breakable block in a range, providing a double-edged weapon to
        to the player, allowing to accomplish their goal or dying by
        their own mistakes."""
    def __init__(self, pos):
        self.position = pos

    def get_position(self):  # Getter
        return self.position

    def set_position(self, pos):  # Setter
        self.position = pos
