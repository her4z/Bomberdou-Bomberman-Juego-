import sys,os
import Map
import pygame
import Background
import View
sys.path.append(os.path.dirname(__file__))

CONTROLS = {'273': [0, -1], '274': [0, 1], '275': [1, 0], '276': [-1, 0]}


class Driver:
    def __init__(self):
        self.dimentions = (800, 600)
        self.map = Map.Map('elnombredeljugador', self.dimentions)
        self.view = View.View(self.dimentions, self.map)
        self.view.load_background('background.jpg')
        self.view.load_image_tntman('../src/pinguino-frente.png')
        self.main_loop()

        

    def main_loop(self):
        while True:
            for event in pygame.event.get():
                print(event)

                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    self.map.move_tm(CONTROLS[str(event.key)])
                    self.view.reload_background()
                    self.view.reload_tntman()
                # self.view.fill([255, 255, 255])
                pygame.display.flip()


if __name__ == "__main__":
    driver = Driver()
    Background = Background("background.jpg", [0, 0])