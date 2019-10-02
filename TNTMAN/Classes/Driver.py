from View import View
from Map import Map
import pygame


class Driver:
    def __init__(self):
        self.dimentions = (800, 600)
        self.map = Map(player_name, self.dimentions,)
        self.view = View(self.dimentions, self.map)
        self.load_imgs()
        self.main_loop()
    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN: 
                    self.map.tntman_moves()


        
