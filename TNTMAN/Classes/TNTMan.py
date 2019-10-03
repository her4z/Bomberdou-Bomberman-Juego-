import Entity


class TNTMan(Entity.Entity):
    def __init__(self, el_nombre):
        super().__init__()
        self.buff = False
        self.name = el_nombre
        self.move_to = None
        self.position = Position

    def deploy_bomb(self):
        pass

    def move(self, direction, is_valid):
        pass

    def get_new_movable_position(self, direction):
        pass

    def get_position():
        return self.position
