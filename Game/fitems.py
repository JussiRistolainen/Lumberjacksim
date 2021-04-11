import pygame
import numpy as np
class Items:

    def __init__(self, window, res_w, res_h):
        self.window = window
        self.res_w = res_w
        self.res_h = res_h

    def create_new_wood_log(self, interpe, object_list):
        for i in range(interpe):
            random_x = np.random.randint(self.res_w - 100)
            random_y = np.random.randint(self.res_h - 100)
            object_list.append([random_x, random_y, 'Log', 0, [random_x-35, random_y-15, random_x+32, random_y+10]])


    def create_new_log_at_pos(self, pos_x, pos_y, object_list):
        object_list.append([pos_x, pos_y, 'Log', 0, [pos_x-35, pos_y-15, pos_x+32, pos_y+10]])


    def lift_item(self, object_list, position):
        del_list = []
        for index, i in enumerate(object_list):
            if i[4][0] < position[0] < i[4][2] and i[4][1] < position[1] < i[4][3]:
                del_list.append(index)

        for i in del_list:
            object_list.pop(i)



