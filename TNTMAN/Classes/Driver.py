import Map
import pygame
import View


class Driver:
    def __init__(self):
        self.dimentions = (800, 600)
        self.map = Map.Map("Fede", self.dimentions)
        self.view = View.View(self.dimentions, self.map)
        self.load_imgs()
        self.main_loop()

    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.map.move_tm(CONTROLS[str(event.key)])
                    self.view.reload_background()
                    self.view.reload_tntman()
                pygame.display.flip()

    def load_imgs(self):
        self.view.load_background('background.jpg')
        self.view.load_image_tntman('tmsprite.png', (2, 2))

if __name__ == "__main__":
    driver = Driver()
