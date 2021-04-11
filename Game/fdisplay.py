import pygame


class Display:

    def __init__(self, window,  character_pos, object_list):
        self.window = window
        self.character_pos = character_pos
        self.time = 0
        self.IMAGES = {}
        self.object_list = object_list
        self.object_size = [100, 100, 100, 100, 100, 200, 200, 60, 60, 50]
        self.character_in_radius = 0

    def get_object_list(self, list):
        self.object_list = list

    def get_time(self, clock):
        self.time = clock

    def get_character_in_rad(self, in_rad):
        self.character_in_radius = in_rad



    def load_images(self):
        image_list = ['sprite_', 'sprite2_', 'sprite22_', 'logburn',
                      'spritelog', 'Lumberjack', 'charecter', 'log_index',
                      'matchbox_icon', 'matchbox']
        image_size =  self.object_size
        index_list = [13, 4, 4, 3, 1, 2, 3, 1, 1, 1]
        for index, p in enumerate(image_list):
            for i in range(0, index_list[index]):
                self.IMAGES[p + str(i)] = pygame.transform.scale(
                    pygame.image.load('Game/Images/log/' + p + str(i) + '.png'), (image_size[index], image_size[index]))


    def update(self):
        depth = sorted(self.object_list, key=lambda x: int(x[1]))
        draw_character = 0
        for i in depth:
            if i[3] == 1:
                if i[1] > self.character_pos[1] and draw_character == 0 and self.character_in_radius == 1:
                    draw_character = 1
                    self.draw_sprite(self.object_size[2], 2, 2, 'Lumberjack', self.character_pos[0]-46, self.character_pos[1]-75, 2)
                    #pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(self.character_pos[0]-27, self.character_pos[1]-95,55, 100), 2)
                    #pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(self.character_pos[0], self.character_pos[1], 2, 2), 2)
                if i[2] == 'Log':
                    self.draw_sprite(self.object_size[4], 2, 2, 'spritelog', i[0], i[1])
                    #pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(i[0]-35, i[1]-15, 67, 25), 2)
                if i[2] == 'Matches':
                    self.draw_sprite(self.object_size[4], 2, 2, 'matchbox', i[0], i[1])
                    #pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(i[0]-35, i[1]-33, 28, 20), 2)
                if i[2] == 'fire':
                    if i[5] * 5 < 13:
                        self.draw_sprite(self.object_size[0], 2, 2, 'sprite_', i[0], i[1], 13, 5)
                    elif i[5] < 70:
                        self.draw_sprite(self.object_size[1], 2, 2, 'sprite2_', i[0], i[1], 4, 5)

                    elif i[5] < 120:
                        self.draw_sprite(self.object_size[2], 2, 2, 'sprite22_', i[0], i[1], 4, 5)
                    else:
                        self.draw_sprite(self.object_size[0], 2, 2, 'logburn', i[0], i[1], 3, 5)

        if draw_character == 0 and self.character_in_radius == 1:
            self.draw_sprite(self.object_size[2], 2, 2, 'Lumberjack', self.character_pos[0]-46, self.character_pos[1]-75, 2)
            #pygame.draw.rect(self.window, (255, 255, 255), pygame.Rect(self.character_pos[0]-27, self.character_pos[1]-95,55, 100), 2)
            #self.draw_sprite(self.object_size[2], 2, 2, 'Lumberjack', self.character_pos[0] - 46,self.character_pos[1] - 75, 2)
            draw_character = 1

        self.draw_sprite(self.object_size[7], 2, 2, 'log_index', 150, 25)
        self.draw_sprite(self.object_size[8], 2, 2, 'matchbox_icon', 210, 20)

    def draw_sprite(self, object_size, x_div, y_div, spritename, pos_x, pos_y, mod = 1, speed = 1):
        self.window.blit(self.IMAGES[spritename + str(int(speed*self.time[1] % mod))], (
            pos_x - object_size//x_div,
            pos_y - object_size//y_div))

