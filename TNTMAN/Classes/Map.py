import TNTMan
import View
import sys, os
import Cells
import Bomb
import pygame
sys.path.append(os.path.dirname(__file__))


class Map():
    def __init__(self, player_name, dimentions):
        self.name = player_name
        self.dimentions = dimentions
        self.map_array = None
        self.TNTMan = TNTMan.TNTMan(self.name)

        def build_map_array(self):
            map_array = []
            for x in range (0, 26):
                for y in range (0, 20):
                    map_array.append(Cells.Cells([x, y]))
            self.map_array = map_array
        build_map_array(self)


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
    
    def place_bomb(self, bomb_key):
        if bomb_key == '101':
            print("bomba")
            self.Bomb = Bomb.Bomb()
            self.bomb_pos = self.TNTMan.get_position()
            self.bomb_state = True
            print(self.bomb_pos)
            self.explode_bomb()
            return self.bomb_state

    
    def explode_bomb(self):
        self.bomb_time = pygame.time.get_ticks()
        self.explotion_delay = 200    
        explotion = pygame.time.get_ticks()
        print("explotion", explotion)
        print ("self.bomb_time", self.bomb_time)
        print("self.explotion_delay", self.explotion_delay)
        if explotion - self.bomb_time <= self.explotion_delay:
            self.bomb_time = explotion
            print("explode_bomb correct")
    
        

        
    
    
    

        
