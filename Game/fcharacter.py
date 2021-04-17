import pygame
import math

class Character:

    def __init__(self, character_pos, x_speed, y_speed):
        self.character_pos = character_pos
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update_character_pos(self, change):
        self.character_pos[0] += change[0]
        self.character_pos[1] += change[1]

    def speed(self, x_force, y_force, mass):
        if x_force > 0:
          self.x_speed = 5
        if x_force == 0:
            self.x_speed = 0
        if x_force < 0:
            self.x_speed = -5
        if y_force > 0:
            self.y_speed = 5
        if y_force == 0:
            self.y_speed = 0
        if y_force < 0:
            self.y_speed = -5



        return self.x_speed, self.y_speed


    def get_character_position(self):
        self.character_pos
        return self.character_pos