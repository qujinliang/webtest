class URLCatcher(object):
	def __init__(self):
		self.urls = []
	def add_url(self,url):
		self.urls.append(url)


a = URLCatcher()
a.add_url('http://www.google.com')
b = URLCatcher()
b.add_url('http://www.bbc.co.hk')

print(a.urls)
print(b.urls)
