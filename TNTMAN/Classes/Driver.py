import os       # Import sys and os for python to understand the local
import sys      # directory.
import Map      # Import File 'Map.py'.
import pygame   # Import pygame module.
import View     # Import 'View.py' module.
sys.path.append(os.path.dirname(__file__))

CONTROLS = {'273': [0, -1], '274': [0, 1], '275': [1, 0], '276': [-1, 0]}
""" If any of these arrows are pressed, this dictionary searches for a list,
    which represents """


class Driver:

    """ Driver is the link between Map (the game controller) and the
        View, allowing to represent what happens on the game visually."""

    def __init__(self):

        self.dimentions = (800, 600)  # Defines pixel dimentions of the game.
        # self.clock = pygame.time.Clock()
        # self.bombtime = 0
        self.map = Map.Map(self.dimentions)  # Creates map.
        self.map.build_map_array()  # Creates a cell array for segmenting the
        # map.
        self.view = View.View(self.dimentions, self.map)  # Creates View.
        self.view.load_blocks()  # Load blocks images.
        self.main_loop()  # Calls the main loop.

    def main_loop(self):

        """ Main loop keeps looping over and over as long as the game
            lasts, so everything that needs to be constantly checked
            works"""

        while True:
            # self.clock.tick()

            for event in pygame.event.get():    # Catch all the pygame events.
                print(event)
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:  # If a key is pressed:
                    try:
                        self.map.deploy_bomb(event.key)
                        self.view.load_sprite_bomb(event.key)
                        self.view.change_tntman_sprite(str(event.key))
                        self.map.is_position_valid(CONTROLS[str(event.key)])
                        self.map.move_tm(CONTROLS[str(event.key)])
                    except KeyError:
                        """In case the key pressed isn't expected,
                           raises an error."""
                        pass
                self.view.reload_background()
                self.view.reload_tntman()
                self.view.load_blocks()

                if self.map.is_there_any_bomb() is True:
                    """ In case there is a bomb, the main loop will"""
                    self.view.reload_bomb()

                # self.clock.tick()
                # self.bombtime = self.bombtime + self.clock.get_time()
                # if self.bombtime > 3000:
                # self.map.destroy_bomb()

                pygame.display.flip()  # Updates screen.


if __name__ == "__main__":  # This function runs first.
    driver = Driver()  # Creates the Driver.
