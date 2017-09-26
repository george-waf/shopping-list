'''docstring for app'''
from flask import Flask, session, render_template, request, url_for, redirect
from models import user
import sys

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
@app.route('/sign-up', methods=['POST', 'GET'])
def index():
    '''rendering the sign up page'''
    error = None
    if request.method == 'POST':
        if validate_data(request.form['username'], request.form['email'], request.form['password']):
            new_user = user.user(request.form['username'], request.form['email'], request.form['password'])
            user.add_user(new_user)
            return redirect(url_for('login'))
        else:
            error = 'Invalid format of email or password'
    return render_template('sign-up.html', error=error)

@app.route('/login', methods=['POST', 'GET'])
def login():
    '''Rendering the login page'''
    error = None
    if request.method == 'POST':
        valid_user = validate_login(request.form['email'], request.form['password'])
        if valid_user:
            return log_the_user_in(valid_user)
        else:
            error = 'Wrong email or password'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    '''Rendering the logout page'''
    session.clear()
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    '''Rendering the dashboard page'''    
    verify_user_is_logged_in()
    return render_template('dashboard.html')
        

def validate_data(username, email, password):
    '''validate if email and password are valid'''
    if username and email and password: return True
    else: return False

def validate_login(email, password):
    '''check if user exists in system'''
    return next((obj for obj in user.get_all_users() if obj.email == email and obj.password == password), None)

def log_the_user_in(a_user):
    '''take the user to there dashboard'''
    session["email"] = a_user.email
    session["logged_in"] = True
    return redirect(url_for('dashboard'))

def verify_user_is_logged_in():
    if not session.get("logged_in"):
        return redirect(url_for('login'))

@app.route('/sh_list', methods = ['POST', 'PUT', 'DELETE'])
def add_sh_list():
    '''add a new shopping list'''   
    verify_user_is_logged_in()
    if request.method == 'POST':
        return "added list"
    elif request.method == 'PUT':
        return "updated list"
    elif request.method == 'DELETE':
        return "deleted list"


app.secret_key = 'A0Zr98j/3yX Q~XHH!jmN]LWX/,?RT'

if __name__ == "__main__":
    app.run()
