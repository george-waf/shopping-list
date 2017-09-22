[![Build Status](https://travis-ci.org/Stankim/shopping-list.svg?branch=develop)](https://travis-ci.org/Stankim/shopping-list)	[![Coverage Status](https://coveralls.io/repos/github/Stankim/shopping-list/badge.svg)](https://coveralls.io/github/Stankim/shopping-list)	[![Code Climate](https://codeclimate.com/github/codeclimate/codeclimate/badges/gpa.svg)](https://codeclimate.com/github/codeclimate/codeclimate)	[![Test Coverage](https://codeclimate.com/github/codeclimate/codeclimate/badges/coverage.svg)](https://codeclimate.com/github/codeclimate/codeclimate/coverage)

# Shopping List App
A shopping list app that helps users track and share lists of things they want to spend there money on.
It is made using the Flask framework, python.
You can find the app online [here](https://shoppist.herokuapp.com)

## Installation and Usage
* Clone the repo
```
$ git clone https://github.com/Stankim/shopping-list.git
```
* Switch to the shopping-list folder
```
$ cd shopping-list
```

* Install the required packages:
```
$ pip install -r requirements.txt
```

* Run the app
```
$ export FLASK_APP=index.py
$ flask run
```

Learn more on running a flask app [here](http://flask.pocoo.org/docs/0.12/quickstart/).

## Testing
Make sure you have installed the required packages then:
```
$ nosetests tests/test-app.py
```

## License
### The MIT License (MIT)

Copyright (c) 2017, Stanley Kimau.

