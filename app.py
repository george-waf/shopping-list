'''docstring for APP'''
from flask import Flask, session, render_template, request, url_for, redirect, Response
from models import user, shopping_list, item

APP = Flask(__name__)
APP.config['TEMPLATES_AUTO_RELOAD'] = True


@APP.route('/')
@APP.route('/sign-up', methods=['POST', 'GET'])
def index():
    '''rendering the sign up page'''
    error = None
    if request.method == 'POST':
        error = validate_data(request.form['username'],
                              request.form['email'],
                              request.form['password'],
                              request.form['confirm_password'])
        if not error:
            error = verify_user_data_is_unique(
                request.form['username'], request.form['email'])
        if error:
            return render_template('sign-up.html', error=error)
        new_user = user.User(request.form['username'],
                             request.form['email'],
                             request.form['password'])
        user.add_user(new_user)
        return redirect(url_for('login'))

    elif request.method == 'GET':
        return render_template('sign-up.html')


@APP.route('/login', methods=['POST', 'GET'])
def login():
    '''Rendering the login page'''
    error = None
    if request.method == 'POST':
        valid_user = validate_login(
            request.form['email'], request.form['password'])
        if valid_user:
            return log_the_user_in(valid_user)
        else:
            error = 'Wrong email or password'
    return render_template('login.html', error=error)


@APP.route('/logout')
def logout():
    '''Rendering the logout page'''
    session["logged_in"] = False
    return redirect(url_for('login'))


@APP.route('/dashboard')
def dashboard():
    '''Rendering the dashboard page'''
    verify_user_is_logged_in()
    return render_template('dashboard.html')


def validate_data(username, email, password, confirm_password):
    '''validate if email and password are valid'''
    if not (username and email and password and confirm_password):
        return "Invalid format of username, email or password"
    elif password != confirm_password:
        return "Passwords do not match"
    return None


def verify_user_data_is_unique(username, email):
    if any(user.username == username for user in user.get_all_users()):
        return "That username is already taken"
    if any(user.email == email for user in user.get_all_users()):
        return "Another user is already using that email"
    return None


def validate_login(email, password):
    '''check if user exists in system and return the user object'''
    for each_user in user.get_all_users():
        if each_user.email == email and each_user.password == password:
            return each_user
    return None


def log_the_user_in(user):
    '''take the user to there dashboard'''
    session["email"] = user.email
    session["logged_in"] = True
    return redirect(url_for('dashboard'))


def verify_user_is_logged_in():
    '''check if the user id logged in, if not redirect to login'''
    if not session.get("logged_in"):
        return redirect(url_for('login'))
    return user.get_user_by_email(session['email'])


@APP.route('/item', methods=['POST', 'PUT', 'DELETE'])
def add_item():
    '''add a new shopping list'''
    verify_user_is_logged_in()
    if request.method == 'POST':
        new_item = item.Item(
            request.form['name'],
            request.form['done'])
        item.add_item(new_item)
        resp = Response(response=new_item.id, status=201)
        return resp
    elif request.method == 'PUT':
        return "updated list"
    elif request.method == 'DELETE':
        return "deleted list"


@APP.route('/shopping_list', methods=['POST', 'PUT', 'DELETE'])
def add_shopping_list():
    '''add a new shopping list'''
    user = verify_user_is_logged_in()
    if request.method == 'POST':
        new_shopping_list = shopping_list.ShoppingList(
            request.form['title'],
            make_item_objects_list(request.form['items']), user)
        user.add_shopping_list(new_shopping_list)
        shopping_list.add_shopping_list(new_shopping_list)
        resp = Response(response=new_shopping_list.id, status=201)
        return resp
    elif request.method == 'PUT':
        return "updated list"
    elif request.method == 'DELETE':
        return "deleted list"


def make_item_objects_list(dict_of_items):
    item_objects = []
    for item_name, done in list_of_items.items():
        item_objects.append(item.Item(item_name, done))
    return item_objects

APP.secret_key = 'B0ZR98j/3yX Q~XHH!jmN]LWX/,?IU'

if __name__ == "__main__":
    APP.run()
