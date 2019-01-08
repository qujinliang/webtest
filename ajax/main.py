from flask import Flask,render_template,request,jsonify
import requests
from ajax import THQS

t = THQS.thqs()
app = Flask(__name__)

@app.route("/index")
def index1():
    return render_template('ajaxIndex.html')

@app.route('/ajax')
def ajax():
    return render_template('roomid_list.html')

@app.route('/ajax',methods=['POST'])
def ajax_post():
    return render_template('roomid_list.html')

@app.route('/')
def index():
    return render_template('roomid_list.html')

@app.route('/roomid',methods=['GET','POST'])
def roomid_post():
    if request.method == 'POST':
        url = "https://ccapi.csslcloud.net/api/v1/room/user/list?"
        roomid = request.values['roomid']
        data = {'roomid':roomid}
        data = t.get_thqs(data)
        api = url + data
        r = requests.get(api)
        r = r.text
        try:
            r = r.encode('utf-8').decode('unicode_escape')
            return jsonify(r)
        except Exception as e:
            print(e)
            return r

if __name__ == '__main__':
    app.run(debug=True)