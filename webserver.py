#!/usr/bin/python3

from flask import Flask

myapp = Flask("hello world")

@myapp.route('/')
def hello_world():
	return 'hello world'


if "__main__" == __name__:
	myapp.run(debug=False, host='0.0.0.0')
