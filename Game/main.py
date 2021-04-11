import pygame
import math
from Game.fcharacter import Character
from Game.ftime import Timecount
from Game.fbackground import Background
from Game.fitems import Items
from Game.fdisplay import Display
from fflame import Flame
from fgrid import Grid

def main():
    pygame.init()

    res_w = 1280
    res_h = 720
    window = pygame.display.set_mode((res_w, res_h))
    running = True
    FPS = 30
    block = 30

    #Item list
    object_list = []

    #Class objects
    character = Character([640, 360], 0, 0)
    time_count = Timecount(window, 0, 0, 0, 1)
    background = Background(window, character.get_character_position())
    items = Items(window, res_w, res_h)
    display_refresh = Display(window, character.get_character_position(), object_list)
    flame = Flame(window, 100, 30)


    #GameClock
    Clock = pygame.time.Clock()
    CLOCKTICKFLAME = pygame.USEREVENT + 1
    pygame.time.set_timer(CLOCKTICKFLAME, 100)



    #Load sprites
    display_refresh.load_images()

    #spawn logs
    items.create_new_wood_log(3, object_list)
    flame.create_flame(object_list, 640, 360, 0)

    mouse = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            keys = pygame.key.get_pressed()

            x_force = 0
            y_force = 0
            if keys[pygame.K_LEFT]:
                x_force = -20

            if keys[pygame.K_RIGHT]:
                x_force = 20

            if keys[pygame.K_UP]:
                y_force = -20

            if keys[pygame.K_DOWN]:
                y_force = 20

            character.update_character_pos(character.speed(x_force, y_force, 10))

            pos = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if click[0] == 1 and mouse:
                time_count.update_items(items.lift_item(object_list, pos))
                mouse = 0

            if event.type == CLOCKTICKFLAME:
                time_count.update_time()
                flame.update_time(object_list)
                flame.items_in_radius(object_list)
                display_refresh.get_object_list(object_list)
                display_refresh.get_character_in_rad(
                flame.character_in_radius(character.get_character_position(), object_list))
                display_refresh.get_time(time_count.get_time())
                background.update(object_list)
                display_refresh.update()
                time_count.update_overlay()
                pygame.display.flip()


            if event.type == pygame.MOUSEBUTTONUP:
                mouse = 1







        Clock.tick(FPS)


if __name__ == "__main__":
    main()