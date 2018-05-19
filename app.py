

from flask import Flask

myapp = Flask("hello world")

@myapp.route('/')
def hello_world():
	return 'hello world'


