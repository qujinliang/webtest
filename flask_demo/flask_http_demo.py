from flask import Flask,request,url_for,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'

@app.route('/hello/')
@app.route('/hello/<name>')
# 会把url传的变量,传入html模板中,然后再html中处理完逻辑，再渲染完后返回到这里
def hello(name=None):
    return render_template('hello.html',name=name)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return 'POST请求'
    else:
        return '不是post请求'

if __name__ == '__main__':
    app.run(debug=True)