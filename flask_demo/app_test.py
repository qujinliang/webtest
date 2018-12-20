from flask import Flask,url_for
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world!'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return 'User %s'%username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' %post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' % subpath

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login',next='/'))
    print(url_for('profile',username='John Doe'))


if __name__ == '__main__':
    app.run(debug=True)