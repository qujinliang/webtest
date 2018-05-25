"""
 Created by qujl on 2018-05-25
"""
__author__ = 'qujl'
from blog import app

@app.route('/')
def hello_word():
    return 'hello word'


if __name__ == '__main__':
    app.run(debug=True)