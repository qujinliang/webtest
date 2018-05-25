"""
 Created by qujl on 2018-05-18
"""
__author__ = 'qujl'

from flask import Flask, render_template, request
import requests
import json
import re

app = Flask(__name__)
app.jinja_env.variable_start_string = '{{ '
app.jinja_env.variable_end_string = ' }}'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/query', methods=['POST'])
def query():
    keywords = request.form.get('shopname')
    url_base = "https://list.tmall.com/search_product.htm?q=%s" %keywords
    print(url_base)
    headers = {"User-Agent": "iphone7"}

    try:
        result_base = str(requests.get(url=url_base, headers=headers, timeout=15).text)
        infostr = re.findall(r'j_shop_moreshop_more\">(.+?)</div>', result_base)
        print(infostr)
        shoplist = []

        for item in infostr:
            scorelist = re.findall(r'\">(.+?)</span><iclass=\"', item)
            thisShopname = re.findall(r'<span>(.+?)</span>', item)[0]
            shoplist.append('{"shopname": "' + thisShopname + '" , "dsr": "' + scorelist[0] + '", "service": "' + scorelist[1].split('">')[1] + '","ship": "' + scorelist[2].split('">')[1] + '"}')

        return json.dumps({"code": 0, "rows": list(set(shoplist))})
    except Exception as e:
        print (e)
        return json.dumps({"code": -1, "msg": "没查询到相关店铺"})

if __name__ == "__main__":
    app.run(debug=True)