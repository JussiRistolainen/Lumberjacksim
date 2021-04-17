from fitem import Item
import pygame


def main():
    item = Item(pygame.display.set_mode((0, 0)), 0, 0, "item")
    item2 = Item(pygame.display.set_mode((0, 0)), 4, 0, "item")
    print(item.getDistanceFromPosition(item2))
    print(item.getPositionX)


main()