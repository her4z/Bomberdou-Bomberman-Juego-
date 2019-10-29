import Entity
import View


class TNTMan(Entity.Entity):
    def __init__(self, name, pos=[34, 32]):
        self.actual_pos = pos
        self.name = name
        self.step_size = 32  # Velocity

    def move_to(self, direction, is_valid):  # is_valid is 0 o 1. If valid, 1
        print('is_valid', is_valid)
        for index, item in enumerate(self.actual_pos):
            if(is_valid == 1):
                self.step_size = 32
            else:
                self.step_size = 0
            self.actual_pos[index] = (item + is_valid * self.step_size *
                                      direction[index])

    def get_stepsize(self):
        return self.step_size
  
    def get_new_possible_position(self, direction):
        print('direction', direction)
        aux_list = []
        for index, item in enumerate(self.actual_pos):
            aux_list = (item + self.step_size * int(direction[index]))
        return aux_list
        

    def get_position(self):
        return self.actual_pos
    

        
