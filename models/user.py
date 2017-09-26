class user(object):
    """docstring for user"""
    def __init__(self, email, password, shopping_lists = []):
        self.email = email
        self.password = password
        self.shopping_lists = shopping_lists

    def get(self):
        pass

    def add():
        pass
        
    def delete(self):
        pass

    def update():
        pass

all_users = []

def add_user(user):
    all_users.append(user)

def get_all_users():
    return all_users