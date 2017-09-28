'''module for handling users'''


class User(object):
    """docstring for user"""

    def __init__(self, username, email, password, shopping_lists=[]):
        self.email = email
        self.password = password
        self.username = username
        self.shopping_lists = shopping_lists

    def add_shopping_list(self, shopping_list):
        self.shopping_lists.append(shopping_list)

ALL_USERS = []


def add_user(user):
    '''add a new user to the list'''
    ALL_USERS.append(user)


def get_all_users():
    '''return a list of all users'''
    return ALL_USERS


def get_user_by_email(email):
    for each_user in ALL_USERS:
        if each_user.email == email:
            return each_user
    return None
