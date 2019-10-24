import Entity


class TNTMan(Entity.Entity):
    def __init__(self, name, pos=[34, 32]):
        self.actual_pos = pos 
        self.name= name
        self.step_size = 32 # velocidad

    def move_to(self, direction, is_valid): #es_valida es 0 o 1. Si es valida, es 1
        print('is_valid',is_valid)
        for index, item in enumerate(self.actual_pos):
            self.actual_pos[index] = item+is_valid*self.step_size*direction[index]

    def get_stepsize(self):
        return self.step_size
    
    def get_new_possible_position(self, direction):
        print('direccion',direction)
        aux_list = []
        for index,item in enumerate(self.actual_pos):
            aux_list.append(item+self.step_size*direction[index])
        return aux_list

    def get_position(self):
        return self.actual_pos