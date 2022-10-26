from flask import Flask, request, render_template

app = Flask(__name__)

DEBUG = True


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return render_template('index.html')


@app.route('/user')
def user():
    name = request.args.get('name')
    # if not name:
    #     return '<h1>Bad Request</h1>', 400

    list = ['one', 'two', 'three', 'four']

    return render_template('user.html', name=name, list=list)

