import math
import pygame

class Flame:

    def __init__(self, window, furnace_value, min_value):
        self.window = window
        self.ground = (0, 0, 0)


    def create_flame(self, object_list, pos_x, pos_y, time, size):
        object_list.append([pos_x, pos_y, 'fire', 0, [pos_x-30, pos_y-25, pos_x+30, pos_y+5], time, size])

    def create_fireplace(self, object_list, pos_x, pos_y, time, size):
        object_list.append([pos_x, pos_y, 'fireplace', 0, [pos_x - 60, pos_y - 55, pos_x + 30, pos_y + 35], time, size])

    def create_lantern(self, object_list, pos_x, pos_y, time, size):
        object_list.append([pos_x, pos_y, 'Lantern', 0, [pos_x-30, pos_y-30, pos_x+20, pos_y+20], time, size])
    def craft_flame(self, pos, object_list):
        object_list.append([pos[0], pos[1], 'fire', 0, [pos[0]-55, pos[1]-90, pos[0]-5, pos[1]-20], 0, 3])

    def craft_torch(self, object_list):
        object_list.append([0, 0, 'torch', 0, [0, 0, 0, 0], 0, 1])

    def light_match(self, object_list):
        object_list.append([0, 0, 'torch', 0, [0, 0, 0, 0], 50, 1])


    def items_in_radius(self, object_list):
        flames = []
        for i in object_list:
            i[3] = 0
            if i[2] == 'fire' or 'torch' or 'fireplace' or 'Lantern':
                flames.append(i)
        for i in flames:
            for index, p in enumerate(object_list):
                distance = 5 + math.sqrt(math.pow(p[0] - i[0], 2) + math.pow(p[1] - i[1], 2))
                if i[2] == 'fire' or i[2] == 'torch':
                    if distance < i[6]*150 - i[5] * 1.2:
                        p[3] = 1
                if i[2] == 'fireplace' or i[2] == 'Lantern':
                    if distance < i[6] * 50 - i[5] * 1.2:
                        p[3] = 1

    def character_in_radius(self, pos, object_list):
        flames = []
        is_in_radius = 0
        for i in object_list:
            if i[2] == 'fire' or 'fireplace' or 'Lantern':
                flames.append(i)
        for p in flames:
            distance = math.sqrt(math.pow(p[0] - pos[0], 2) + math.pow(p[1] - pos[1], 2))
            if p[2] == 'fire':
                if distance < p[6]*150 - p[5] * 1.2:
                    is_in_radius = 1
            if p[2] == 'fireplace' or p[2] == 'Lantern':
                if distance < p[6]*50 - p[5] * 1.2:
                    is_in_radius = 1
        return is_in_radius


    def update_time(self, object_list):
        del_fire = []
        for index, i in enumerate(object_list):
            if i[2] == 'fire' or i[2] == 'torch' or i[2] == "fireplace" or i[2] == 'Lantern':
                i[5] += 0.1
                if i[5] > 60:
                    i[6] -= 1
                    i[5] = 0
                if i[6] == 0:
                    del_fire.append(index)
        for i in del_fire:
            object_list.pop(i)






