'''module for handling shopping lists'''
class ShoppingList(object):
    """docstring for shopping_list"""

    def __init__(self, title, items, owner):
        self.title = title
        self.items = items
        self.owner = owner
