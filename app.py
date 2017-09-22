'''docstring for app'''
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
@app.route('/sign-up', methods=['POST', 'GET'])
def index():
    '''rendering the sign up page'''
    error = None
    if request.method == 'POST':
        if validate_data(request.form['email'], request.form['password']):
            return log_the_user_in(request.form['email'])
        else:
            error = 'Invalid format of email or password'
    return render_template('sign-up.html', error=error)

@app.route('/login', methods=['POST', 'GET'])
def login():
    '''Rendering the login page'''
    error = None
    if request.method == 'POST':
        if valid_login(request.form['email'], request.form['password']):
            return log_the_user_in(request.form['email'])
        else:
            error = 'Wrong email or password'
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    '''Rendering the dashboard page'''
    return render_template('dashboard.html')


def validate_data(email, password):
    if email and password: return True
    else: return False

def valid_login(email, password):
    if email == "user@shoppist.com" and password == "qwerty":
        return True
    else: return False

def log_the_user_in(email):
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run()
