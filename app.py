'''docstring for APP'''
from flask import Flask, session, render_template, request, url_for, redirect
from models import user

APP = Flask(__name__)
APP.config['TEMPLATES_AUTO_RELOAD'] = True


@APP.route('/')
@APP.route('/sign-up', methods=['POST', 'GET'])
def index():
    '''rendering the sign up page'''
    some_error = None
    if request.method == 'POST':
        some_error = validate_data(request.form['username'],
                                   request.form['email'],
                                   request.form['password'],
                                   request.form['confirm_password'])
        if not some_error:
            new_user = user.User(request.form['username'],
                                 request.form['email'],
                                 request.form['password'])
            user.add_user(new_user)
            return redirect(url_for('login'))
        return render_template('sign-up.html', error=some_error)
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


def validate_login(email, password):
    '''check if user exists in system and return the user object'''
    return next((obj for obj in user.get_all_users()
                 if obj.email == email and obj.password == password), None)


def log_the_user_in(a_user):
    '''take the user to there dashboard'''
    session["email"] = a_user.email
    session["logged_in"] = True
    return redirect(url_for('dashboard'))


def verify_user_is_logged_in():
    '''check if the user id logged in, if not redirect to login'''
    if not session.get("logged_in"):
        return redirect(url_for('login'))


@APP.route('/sh_list', methods=['POST', 'PUT', 'DELETE'])
def add_sh_list():
    '''add a new shopping list'''
    verify_user_is_logged_in()
    if request.method == 'POST':
        return "added list"
    elif request.method == 'PUT':
        return "updated list"
    elif request.method == 'DELETE':
        return "deleted list"


APP.secret_key = 'B0ZR98j/3yX Q~XHH!jmN]LWX/,?IU'

if __name__ == "__main__":
    APP.run()
