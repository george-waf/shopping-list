'''docstring for app'''
from flask import Flask, session, render_template, request, url_for, redirect
from models import user

app = Flask(__name__)

@app.route('/')
@app.route('/sign-up', methods=['POST', 'GET'])
def index():
    '''rendering the sign up page'''
    error = None
    if request.method == 'POST':
        if validate_data(request.form['email'], request.form['password']):
            a_user = user.user(request.form['email'], request.form['password'])
            #store user in session
            session["email"] = a_user.email
            session["password"] = a_user.password
            return log_the_user_in(a_user)
        else:
            error = 'Invalid format of email or password'
    return render_template('sign-up.html', error=error)

@app.route('/login', methods=['POST', 'GET'])
def login():
    '''Rendering the login page'''
    error = None
    if request.method == 'POST':
        if valid_login(request.form['email'], request.form['password']):
            #creeate a new user
            a_user = user.user(request.form['email'], request.form['password'])
            #store user in session
            session["email"] = a_user.email
            session["password"] = a_user.password
            return log_the_user_in(a_user)
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
    if session.get("logged_in"):
        a_user = user.user(session["email"], session["password"])
        return render_template('dashboard.html')
    else:
        return redirect(url_for('login'))

def validate_data(email, password):
    '''validate if email and password are valid'''
    if email and password: return True
    else: return False

def valid_login(email, password):
    '''check if user exists in system'''
    if email == "user@shoppist.com" and password == "qwerty":
        return True
    else: return False

def log_the_user_in(a_user):
    '''take the user to there dashboard'''
    session["logged_in"] = True
    return redirect(url_for('dashboard'))


app.secret_key = 'A0Zr98j/3yX Q~XHH!jmN]LWX/,?RT'

if __name__ == "__main__":
    app.run()
