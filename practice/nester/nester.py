import os
import sys

"""这是list_ex.py模块，提供了一个名为print_lol()的函数，这个函数作用时打印列表，其中有可能包含（也可能不包含）嵌套列表。"""


#moves = ["The Holy Graill", 1975, "Terry Jones & Terry Gilliam",91,
#			["Graham Chapman", ["Michael Palin","John Cleese","Terry Gilliam","Eric Idle","Terry Jones"]]]



def print_lol(the_list,indent=False,level=0, fn=sys.stdout):
	"""这个函数取一个位置参数，名为'the_list',这可以是任何python列表（也可以是包含嵌套列表的列表）。所指定的列表中的每个
	数据项会（递归地）输出到屏幕上，各数据项各占一行。"""
	for each_item in the_list:
		if isinstance(each_item,list):
			print_lol(each_item,indent,level+1,fn)

		else:
			if indent == True:
				for num in range(level):
					print("\t",end='',file=fn)
			print(each_item,file=fn)

