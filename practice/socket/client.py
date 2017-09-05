import socket
import sys

#创建socket对象
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#获取本地主机名, mac系统不能用
host = socket.gethostname()

#设置端口号
port = 9999

#连接服务器，指定主机和端口
s.connect(('127.0.0.1',port))

#接受小于1024字节的数据
msg = s.recv(1024)

s.close()

print(msg.decode('utf-8'))