class Cells():
    """ Cells are the minimum part in which the map is divided. These
    create a grid used by the Map."""
    def __init__(self, pos, content):
        self.size = (32, 32)  # Pixel size
        self.content = content
        self.position = []
        self.position = pos
