import Entity
import View


class TNTMan(Entity.Entity):
    def __init__(self, name, pos=[1, 1]):
        self.actual_pos = pos
        self.name = name
        self.step_size = 16  # Velocity

    def move_to(self, direction, is_valid):  # is_valid is 0 o 1. If valid, 1
        self.actual_pos[0] = self.actual_pos[0] + direction[0]
        self.actual_pos[1] = self.actual_pos[1] + direction[1]

    def get_stepsize(self):
        return self.step_size

    def get_new_possible_position(self, direction):
        aux_list = [1, 1]
        aux_list[0] = self.actual_pos[0] + direction[0]
        aux_list[1] = self.actual_pos[1] + direction[1]

        #for index, item in enumerate(self.actual_pos):  # como una posicion es una lista [x,y], este for la recorre.
            #aux_list.append(item + self.step_size * int(direction[index]))
        return aux_list

    def get_position(self):
        return self.actual_pos
