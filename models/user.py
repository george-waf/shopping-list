'''module for handling users'''


class User(object):
    """docstring for user"""

    def __init__(self, username, email, password, shopping_lists=[]):
        self.email = email
        self.password = password
        self.username = username
        self.shopping_lists = shopping_lists

ALL_USERS = []


def add_user(user):
    '''add a new user to the list'''
    ALL_USERS.append(user)


def get_all_users():
    '''return a list of all users'''
    return ALL_USERS
