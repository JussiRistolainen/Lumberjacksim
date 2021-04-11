import math
import pygame

class Flame:

    def __init__(self, window, furnace_value, min_value):
        self.window = window
        self.ground = (0, 0, 0)
        self.furnace_value = furnace_value
        self.min_value = min_value


    def create_flame(self, object_list, pos_x, pos_y, time):
        object_list.append([pos_x, pos_y, 'fire', 0, [0, 0, 0, 0], time])


    def items_in_radius(self, object_list):
        flames = []
        for i in object_list:
            i[3] = 0
            if i[2] == 'fire':
                flames.append(i)
        for i in flames:
            for index, p in enumerate(object_list):
                distance = 5+math.sqrt(math.pow(p[0]-i[0], 2) + math.pow(p[1]-i[1], 2))
                if distance < 500-i[5]*1.2:
                    p[3] = 1


    def update_time(self, object_list):
        for i in object_list:
            if i[2] == 'fire':
                i[5] += 0.1






