from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/signin',methods=['GET'])
def sigin_form():
    return render_template('signin.html')

@app.route('/signin',methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == '1234567':
        return render_template('admin_home.html')
    return render_template('bad.html')

if __name__ == '__main__':
    app.run(debug=True)