'''docstring for app'''
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/sign-up')
def index():
    '''rendering the sign up page'''
    return render_template('sign-up.html')

@app.route('/login')
def login():
    '''Rendering the login page'''
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    '''Rendering the dashboard page'''
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run()
