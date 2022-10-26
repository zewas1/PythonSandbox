from flask import Flask
from flask import request

app = Flask(__name__)

DEBUG = True


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {} </p>'.format(user_agent)


@app.route('/user')
def user():
    name = request.args.get('name')
    if not name:
        return '<h1>Bad Request</h1>', 400
    return '<h1>Hello, {}!</h1>'.format(name), 200

