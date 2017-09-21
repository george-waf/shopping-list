'''docstring for app'''
from flask import Flask
from flask import render_template

APP = Flask(__name__)

@APP.route('/')
@APP.route('/sign-up')
def index():
    '''rendering the sign up page'''
    return render_template('sign-up.html')

@APP.route('/login')
def login():
    '''Rendering the login page'''
    return render_template('login.html')

@APP.route('/dashboard')
def dashboard():
    '''Rendering the dashboard page'''
    return render_template('dashboard.html')

if __name__ == "__main__":
    APP.run()
