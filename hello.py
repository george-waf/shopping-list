'''docstring for app'''
from flask import Flask
APP = Flask(__name__)

@APP.route('/')
def hello_world():
    '''docstring for function'''
    return 'Hello, World!'

if __name__ == "__main__":
    APP.run()
