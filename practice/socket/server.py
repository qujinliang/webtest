import socket
import sys

#创建socket对象
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#获取本地主机名, mac系统不能用
host = socket.gethostname()

port = 9999

#绑定端口
serversocket.bind(('127.0.0.1',port))

#设置最大连接数，超过后排队
serversocket.listen(5)


while True:
	#建立客户段连接
	clientsocket,addr = serversocket.accept()

	print("连接地址: %s" % str(addr))

	msg='欢迎访问菜鸟教程！' + "\r\n"
	clientsocket.send(msg.encode('utf-8'))
	clientsocket.close()