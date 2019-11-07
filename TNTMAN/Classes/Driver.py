import sys
import os
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
        self.clock = pygame.time.Clock()
        self.bombtime = 0
        self.main_loop()

    def main_loop(self):
        while True:
            self.clock.tick()
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    try:
                        self.map.deploy_bomb(event.key)
                        self.view.load_sprite_bomb(event.key)
                        self.view.cambiar_sprite_tntman(str(event.key))
                        self.map.is_position_valid(CONTROLS[str(event.key)])
                        self.map.move_tm(CONTROLS[str(event.key)])
                    except KeyError:
                        pass
                self.view.reload_background()
                self.view.reload_tntman()

                if self.map.is_there_any_bomb() is True:
                    self.view.reload_bomb()
                self.clock.tick()
                self.bombtime = self.bombtime + self.clock.get_time()
                #if self.bombtime > 3000:
                    #self.map.destroy_bomb()
                pygame.display.flip()


if __name__ == "__main__":
    driver = Driver()
    Background = Background("background.jpg", [0, 0])
