'''module for handling shopping lists'''


class ShoppingList(object):
    """docstring for shopping_list"""
    next_id = 0

    def __init__(self, title, items, owner):
        self.title = title
        self.items = items
        self.owner = owner
        self.id = self.get_next_id()

    def get_next_id(self):
        ShoppingList.next_id += 1
        return ShoppingList.next_id

ALL_SHOPPING_LISTS = []


def add_shopping_list(shopping_list):
    ALL_SHOPPING_LISTS.append(shopping_list)
