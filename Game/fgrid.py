import math
import numpy as np


class Grid:

    def __init__(self, res_w, res_h, window, block):
        self.res_w = res_w
        self.res_h = res_h
        self.window = window
        self.block = block

    def grid(self):
        grid_map = []
        for x in range(0, self.res_w, self.block):
            grid_map_x = []
            for y in range(0, self.res_h, self.block):
                grid_map_x.append(0)
            grid_map.append(grid_map_x)
        return grid_map

    def get_pos_in_grid(self, pos):
        x = math.floor(pos[0] / self.block)
        y = math.floor(pos[1] / self.block)
        return x, y

    def get_pos_from_grid(self, pos):
        x = pos[0]*self.block
        y = pos[1]*self.block
        return [x, y]



    def update_item_grid(self, object_list, grid):
        for i in object_list:
            grid_pos = self.get_pos_in_grid([i[0], i[1]])
            if i[2] == "Log":
                grid[grid_pos[0]][grid_pos[1]] = 1
            if i[2] == 'fire':
                grid[grid_pos[0]][grid_pos[1]] = 2







