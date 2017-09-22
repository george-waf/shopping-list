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
        if validate_data(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid format of username or password'
    return render_template('sign-up.html', error=error)

@app.route('/login')
def login():
    '''Rendering the login page'''
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'username or password not correct'
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    '''Rendering the dashboard page'''
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run()
