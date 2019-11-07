import sys,os
import Map
import pygame
import View
sys.path.append(os.path.dirname(__file__))

CONTROLS = {'273': [0, -1], '274': [0, 1], '275': [1, 0], '276': [-1, 0]}


class Driver:
    def __init__(self):
        self.dimentions = (800, 600)
        self.map = Map.Map('elnombredeljugador', self.dimentions)
        self.view = View.View(self.dimentions, self.map)
        self.view.load_background('../src/background.png')
        self.view.load_sprite_tntman("")
        self.view.reload_background()
        self.view.reload_tntman()
        self.main_loop()

    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    try:
                        print(event)
                        print("key:", str(event.key))
                        self.map.move_tm(CONTROLS[str(event.key)])
                        self.map.is_position_valid(CONTROLS[str(event.key)])
                        self.view.cambiar_sprite_tntman(str(event.key))
                    except KeyError:
                        pass
                if event.type == pygame.KEYUP:
                    if str(event.key) == '101':
                        try:
                            self.map.place_bomb(str(event.key))
                            # self.view.load_sprite_bomb()
                            self.view.reload_bomb()
                        except KeyError:
                            pass
                self.view.reload_background()
                self.view.reload_tntman()
                self.view.reload_bomb()
                pygame.display.flip()

if __name__ == "__main__":
    driver = Driver()
