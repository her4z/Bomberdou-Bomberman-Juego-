import TNTMan
import View
import sys, os
sys.path.append(os.path.dirname(__file__))

class Map():
    def __init__(self, player_name, dimentions):
        self.name = player_name
        self.dimentions = dimentions
        self.TNTMan = TNTMan.TNTMan(self.name)
        self.view = View.View(self.dimentions, self.name)
        black = (0, 0, 0)
        rectangle_stuff = (32, 32, 736, 544)
        #self.rectangle = pygame.draw.rect(self.view.screen, black, , 1)

    def is_position_valid(self, direction):
        new_position = self.TNTMan.get_new_possible_position(direction)
        xpos = new_position[0]
        ypos = new_position[1] 
        print("next_pos", new_position)
        if(xpos > 32 and xpos < 768 and ypos > 30 and ypos < 576):
            self.move_tm(direction)
        else:
            pass

    def get_position_tntman(self):
        return self.TNTMan.get_position()

    def move_tm(self, direction):
        self.TNTMan.move_to(direction, 1)
    

           