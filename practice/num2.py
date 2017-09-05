#coding:UTF-8
import re
import urllib.request

def getHtml(url):
	page = urllib.request.urlopen(url)
	html = page.read()
	z_html = html.decode('UTF-8')
	return z_html

def getNum(z_html):
	reg = r'已归档'
	numre = re.compile(reg)
	numlist = re.findall(numre,z_html)
	return numlist

html = getHtml("http://139.217.5.58/invoicesCheck/dist/html/list/index.html")

#print (getNum(html))
print (html)