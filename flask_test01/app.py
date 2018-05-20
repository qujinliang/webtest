from flask import Flask,url_for,request,redirect
from flask import render_template
from flask_test01.view.db_test import DbTest
'''
url地址发送请求，参数username，调用方法prt_name
再调用数据库连接池，然后返回查询到的数据，再传给前段页面展示
'''
app = Flask(__name__)

@app.route('/')
def check():
    return render_template('check.html')

@app.route('/hello/<username>')
def prt_name(username):
    db = DbTest()
    user = db.db_data(username)
    # html模版中判断的是 name
    return render_template('hello1.html',name=user)


# 第一次请求是GET，所以一定要判断啊！！！在表单请求才是POST
@app.route('/check',methods=["GET", "POST"])
def show_post():

    # 请求URL，是GET方法。然后返回表单页面
    if request.method == 'GET':
        return render_template('check.html')

    # 抓去表单页面提交的信息
    post_name = request.form.get('user')
    if post_name:
        return redirect(url_for('prt_name',username=post_name))
    return render_template('check.html')


with app.test_request_context():
    pass
    # print(url_for('prt_name',username='jo'))
    # print(url_for('static', filename='style.css'))
    # print(url_for('show_post',filename='qujl'))

if __name__ == '__main__':
    app.run(debug=True)
