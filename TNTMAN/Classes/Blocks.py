class Blocks():
    def __init__(self):
        self.can_be_broken: None


class BUnbreakable(Blocks):
    def __init__(self):
        self.live = True
        self.life = 100

    def die(self):
        self.live = False
