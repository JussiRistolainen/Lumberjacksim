import pygame


class Display:

    def __init__(self, window,  character_pos, object_list, icon):
        self.window = window
        self.character_pos = character_pos
        self.time = 0
        self.IMAGES = {}
        self.object_list = object_list
        self.object_size = [100, 100, 100, 100, 100, 200, 200, 60,
                            60, 50, 50, 50, 150, 40, 40, 40, 40, 40, 40]
        self.character_in_radius = 0
        self.icon = icon

    def update_objects(self, object):
        self.object_list = object

    def update_variables(self, clock, in_rad):
        self.time = clock
        self.character_in_radius = in_rad

    def icon_checked(self, pos):
        if 2 < pos[0] < 37 and 275 < pos[1] < 310:
            self.icon = 1
        elif 2 < pos[0] < 37 and 320 < pos[1] < 355:
            self.icon = 2
        elif 2 < pos[0] < 37 and 360 < pos[1] < 385:
            self.icon = 3
        elif 2 < pos[0] < 37 and 390 < pos[1] < 415:
            self.icon = 4
        else:
            self.icon = 0

    def update_torch(self, object_list):
        for i in object_list:
            if i[2] == 'torch':
                i[0] = self.character_pos[0]
                i[1] = self.character_pos[1]



    def get_icon(self):
        return self.icon



    def load_images(self):
        image_list = ['sprite_', 'sprite2_', 'sprite22_', 'logburn',
                      'spritelog', 'Lumberjack', 'charecter', 'log_index',
                      'matchbox_icon', 'matchbox', 'bondfire_icon', 'bondfire_icon_checked',
                      'Lumberjack_fire', 'torch', 'torch_checked', 'match_icon', 'match_icon_checked',
                      'log_icon', 'log_icon_checked']
        image_size =  self.object_size
        index_list = [13, 4, 4, 3, 1, 2, 3, 1, 1, 1, 1, 1, 3, 1, 1,1,1,1,1, 1, 1]
        for index, p in enumerate(image_list):
            for i in range(0, index_list[index]):
                self.IMAGES[p + str(i)] = pygame.transform.scale(
                    pygame.image.load('Game/Images/log/' + p + str(i) + '.png'), (image_size[index], image_size[index]))


    def update(self):
        depth = sorted(self.object_list, key=lambda x: int(x[1]))
        draw_character = 0
        torch = 0
        for k in depth:
            if k[2] == 'torch':
                torch = 1

        for i in depth:
            if i[3] == 1:
                if i[1] > self.character_pos[1] and draw_character == 0 and self.character_in_radius == 1 and torch == 0:
                    draw_character = 1
                    self.draw_sprite(self.object_size[2], 2, 2, 'Lumberjack', self.character_pos[0]-46, self.character_pos[1]-75, 2)
                    #pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(self.character_pos[0]-27, self.character_pos[1]-95,55, 100), 2)
                    #pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(self.character_pos[0], self.character_pos[1], 2, 2), 2)
                if i[1] > self.character_pos[1] and draw_character == 0 and torch == 1:
                    draw_character = 1
                    self.draw_sprite(self.object_size[2], 2, 2, 'Lumberjack_fire', self.character_pos[0] - 24, self.character_pos[1] - 50, 3)
                if i[2] == 'Log':
                    self.draw_sprite(self.object_size[4], 2, 2, 'spritelog', i[0], i[1])
                    #pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(i[0]-35, i[1]-15, 67, 25), 2)
                if i[2] == 'Matches':
                    self.draw_sprite(self.object_size[4], 2, 2, 'matchbox', i[0], i[1])
                    #pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(i[0]-35, i[1]-33, 28, 20), 2)
                if i[2] == 'fire':
                    if i[5]*5 < 12 and i[6] == 3:
                        self.draw_fire(self.object_size[0], 2, 2, 'sprite_', i[0], i[1], i[5], 13, 5)
                    elif i[6] == 3:
                        self.draw_sprite(self.object_size[1], 2, 2, 'sprite2_', i[0], i[1], 4, 5)

                    elif i[6] == 2:
                        self.draw_sprite(self.object_size[2], 2, 2, 'sprite22_', i[0], i[1], 4, 5)
                    elif i[6] == 1 and (i[5] < 57 or  57.5 < i[5] < 58.5 or 59 < i[5] < 95.5):
                        self.draw_sprite(self.object_size[0], 2, 2, 'logburn', i[0], i[1], 3, 5)

        if draw_character == 0 and self.character_in_radius == 1 and torch == 0:
            self.draw_sprite(self.object_size[2], 2, 2, 'Lumberjack', self.character_pos[0]-46, self.character_pos[1]-75, 2)
            #pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(self.character_pos[0]-27, self.character_pos[1]-95,55, 100), 2)
            #self.draw_sprite(self.object_size[2], 2, 2, 'Lumberjack', self.character_pos[0] - 46,self.character_pos[1] - 75, 2)
            draw_character = 1
        if draw_character == 0 and torch == 1:
            draw_character = 1
            self.draw_sprite(self.object_size[2], 2, 2, 'Lumberjack_fire', self.character_pos[0] - 24, self.character_pos[1] - 50, 3)

        self.draw_sprite(self.object_size[7], 2, 2, 'log_index', 150, 25)
        self.draw_sprite(self.object_size[8], 2, 2, 'matchbox_icon', 210, 20)
        if self.icon != 1:
            self.draw_sprite(self.object_size[9], 2, 2, 'bondfire_icon', 20, 300)
        elif self.icon == 1:
            self.draw_sprite(self.object_size[10], 2, 2, 'bondfire_icon_checked', 20, 300)
        if self.icon != 2:
            self.draw_sprite(self.object_size[13], 2, 2, 'torch', 20, 337)
        elif self.icon == 2:
            self.draw_sprite(self.object_size[14], 2, 2, 'torch_checked', 20, 337)
        if self.icon != 3:
            self.draw_sprite(self.object_size[13], 2, 2, 'match_icon', 17, 370)
        elif self.icon == 3:
            self.draw_sprite(self.object_size[15], 2, 2, 'match_icon_checked', 17, 370)
        if self.icon != 4:
            self.draw_sprite(self.object_size[13], 2, 2, 'log_icon', 20, 400)
        elif self.icon == 4:
            self.draw_sprite(self.object_size[15], 2, 2, 'log_icon_checked', 20, 400)
        pygame.draw.rect(self.window, (55, 55, 55), pygame.Rect(2, 390, 35, 25), 2)


    def draw_sprite(self, object_size, x_div, y_div, spritename, pos_x, pos_y, mod = 1, speed = 1):
        self.window.blit(self.IMAGES[spritename + str(int(speed*self.time[1] % mod))], (
            pos_x - object_size//x_div,
            pos_y - object_size//y_div))


    def draw_fire(self, object_size, x_div, y_div, spritename, pos_x, pos_y, time, mod = 1, speed = 1):
        self.window.blit(self.IMAGES[spritename + str(int(speed * time % mod))], (
            pos_x - object_size // x_div,
            pos_y - object_size // y_div))

