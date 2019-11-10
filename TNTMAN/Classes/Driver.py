import os       # Import sys and os for python to understand the local
import sys      # directory.
import Map      # Import File 'Map.py'.
import pygame   # Import pygame module.
import View     # Import 'View.py' module.
sys.path.append(os.path.dirname(__file__))

CONTROLS = {'273': [0, -1], '274': [0, 1], '275': [1, 0], '276': [-1, 0]}
# These strings refer each one to an arrow key, so Pygame can understand.


class Driver:

    """ Driver is the link between Map (
        the game controller) and the
        View, allowing to represent what happens on the game visually."""

    def __init__(self):

        self.dimentions = (800, 600)    # Defines pixel dimentions of the game
        #  window.
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

            for event in pygame.event.get():    # Catch all the pygame events
                # that will happen.
                print(event)  # Prints every event that happens.
                if event.type == pygame.QUIT:  # Closes the window if the
                    quit()                    # pygame event QUIT is received.
                if event.type == pygame.KEYDOWN:  # If a key is pressed:
                    try:
                        self.map.deploy_bomb(event.key)  # Tells Map class to
                        # deploy the bomb.
                        self.view.load_sprite_bomb(event.key)  # Tells View
                        # class to load the bomb sprite.
                        self.view.change_tntman_sprite(str(event.key))  # Tells
                        # View class to change the tntman sprite.
                        self.map.is_position_valid(CONTROLS[str(event.key)])
                        # Ask Map class if the position is valid for the tntman
                        # to move there.
                        self.map.move_tm(CONTROLS[str(event.key)])  # Tells Map
                        # class to move the tntman.
                    except KeyError:  # If the key pressed isn't the expected
                        pass         # it raises this error.
                self.view.reload_background()  # Tells View class to
                # reload background image.
                self.view.reload_tntman()  # Tells View class to
                # reload tntman character image.
                self.view.load_blocks()  # Tells View class to
                # load blocks images again.

                if self.map.is_there_any_bomb() is True:  # Ask Map class
                    # if there is any bomb, if it does:
                    self.view.reload_bomb()  # Tells View class to reload
                    # bomb image.

                # self.clock.tick()
                # self.bombtime = self.bombtime + self.clock.get_time()
                # if self.bombtime > 3000:
                # self.map.destroy_bomb()

                pygame.display.flip()  # Updates screen.


if __name__ == "__main__":  # This function runs first.
    driver = Driver()  # Creates the Driver.
