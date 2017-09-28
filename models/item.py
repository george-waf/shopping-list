'''a item handling module'''


class Item(object):
    """docstring for item"""
    next_id = 0

    def __init__(self, name, done=False):
        self.name = name
        self.done = done
        self.id = self.get_next_id()

    def get_next_id(self):
        Item.next_id += 1
        return Item.next_id
        
ALL_ITEMS = []


def add_item(item):
    ALL_ITEMS.append(item)
