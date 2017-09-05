#-*- coding:UTF-8 -*-

class _def():
	def hello():
		print ("Hello World!")

	def area(width,height):
		return width * height

	def print_welcome(name):
		print("Welcome",name)

	def printme( str ):
		"打印任何传入的字符串"
		print (str);
		return;

	def changeme( mylist ):
		mylist.append([1,2,3,4]);
		print ("函数内取值： ",mylist)
		return

	def printinfo( name, age ):
		"打印任何传入的字符串"
		print ("名字: ", name);
		print ("年龄： ", age);
		return;

	def printinfo2( arg1, *vartuple ):
		"打印任何传入的参数"
		print ("输出：")
		print (arg1)
		for var in vartuple:
			print (var)

		return;

	# 匿名函数
	sum = lambda arg1, arg2 : arg1 + arg2;

	g = lambda x, y : x**2 + y**2

	total = 0;
	def sum( arg1, arg2 ):
		total = arg1 + arg2;
		print ("函数内是局部变量 : ", total)
		return total;

	
	def test():
		global a
		a = a + 1
		print (a)

	# 把N个关键字参数转化为字典：
	def func(country,property,**kwargs):
		print (country,property,kwargs)





if __name__ == '__main__':
	# _def.hello()
	# _def.print_welcome("Runoob")
	# w = 4
	# h = 5
	# print("width =", w, " height =", h, "area =", _def.area(w, h))

	# _def.printme("我要调用用户的自定义地图");
	# mylist = [10];
	# _def.changeme( mylist );
	# print ("函数外取值： ", mylist)
	# _def.printinfo(age = 50, name="runoob")
	# _def.printinfo2(70,60,50)
	# print ("相加后的值为 ：", _def.sum( 10, 20))

	# _def.sum(10, 20 );
	# print ("函数外是全局变量 : ", _def.total)
	# a = 10
	# _def.test()
	_def.func("China", "Sichuan", city = "Chengdu", section = "JingJiang")
	print (_def.g(2,3))

