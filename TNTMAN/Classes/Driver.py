import sys
import os
import Map
import pygame
import View
sys.path.append(os.path.dirname(__file__))

CONTROLS = {'273': [0, -1], '274': [0, 1], '275': [1, 0], '276': [-1, 0]} 
  # These strings refer each one to an arrow key, so Pygame can understand.


class Driver:
    """ Driver is the link between Map (the game controller) and the
        View, allowing to represent what happens on the game visually."""
    def __init__(self):  
        self.dimentions = (800, 600)
        self.map = Map.Map(self.dimentions)  # Creates map.
        self.view = View.View(self.dimentions, self.map) # Creates View.
        self.main_loop()  #Calls the main loop.

    def main_loop(self):
        """ Main loop keeps looping over and over as long as the game
            lasts, so everything that needs to be constantly checked
            works"""
        while True:
            for event in pygame.event.get():
                print(event)  # Prints every event that happens
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:  # If a key is pressed
                    try:
                        self.map.is_position_valid(CONTROLS[str(event.key)]) 
                        self.map.move_tm(CONTROLS[str(event.key)])
                        self.view.change_tntman_sprite(str(event.key))
                    except KeyError:
                        pass
                    
                self.view.reload_background()  # Reloads background
                self.view.reload_tntman()  # Reloads character
                pygame.display.flip()  # Updates screen

if __name__ == "__main__":  # This function runs first. 
    driver = Driver()  # Creates the Driver
