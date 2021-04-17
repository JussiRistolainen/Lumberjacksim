from fposition import Position


class Item(Position):
    def __init__(self, window, x, y, name):
        super(Item, self).__init__(x, y)
        self.window = window
        self.name = name