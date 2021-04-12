import pygame
import numpy as np
class Items:


    def __init__(self, window, res_w, res_h):
        self.window = window
        self.res_w = res_w
        self.res_h = res_h

    def create_new_item(self, interpe, object_list, name):
        for i in range(interpe):
            random_x = np.random.randint(self.res_w - 100)
            random_y = np.random.randint(self.res_h - 100)
            if name == 'Log':
                object_list.append([random_x, random_y, name, 0, [random_x-35, random_y-15, random_x+32, random_y+10]])
            if name == 'Matches':
                object_list.append([random_x, random_y, name, 0, [random_x - 35, random_y - 33, random_x - 7, random_y - 13]])


    def create_new_log_at_pos(self, pos_x, pos_y, object_list):
        object_list.append([pos_x, pos_y, 'Log', 0, [pos_x-35, pos_y-15, pos_x+32, pos_y+10]])










