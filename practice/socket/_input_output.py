from urllib import request

class _input(object):
	"""docstring for _input"""
	def open():
		f = open('foo.txt','w')
		print("文件名为： ",f.name)
		fid = f.fileno()
		print("文件描述符为: ",fid)
		f.write('python是一个非常好的语言')
		f.close()

	def read():
		f = open('foo.txt','r')
		str = f.read()
		print(str)
		f.close()

	def pachong():
		response = request.urlopen("http://www.baidu.com/")
		fi = open("project.txt",'w')
		page = fi.write(str(response.read()))
		fi.close()

if __name__ == '__main__':
	 _input.open()
	# _input.read()
	#_input.pachong()