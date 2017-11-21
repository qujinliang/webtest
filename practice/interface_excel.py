#coding=utf-8

import xlrd
import time
import xlwt
from xlutils3.copy import copy
import os

def readexcel_date(sheet_value,row_key,row_value):
	#获取当前文件夹的父目录绝对路径
	BASE_DIR = os.path.dirname(os.path.dirname(__file__))
	#展示绝对路径
	print(BASE_DIR)
	#合并当前路径
	filename = os.path.join(BASE_DIR,'test_date/','interface.xlsx')
	#打开工作薄
	date = xlrd.open_workbook(filename)
	#选择工作页
	sheet = date.sheet_by_index(sheet_value)


	#读取行列数据
	date_key = sheet.row_values(row_key)
	date_value = sheet.row_values(row_value)

	#因为从excel读出来的都是float类型，所以需要转换一下
	nos = []
	for i in date_value:
		if i == 0.0:
			nos.append(i)
		elif i == '':
			nos.append(i)
		else:
			no = str(int(i))
			nos.append(no)
	#print(nos)

	#将两个数组合并成字典
	date_dict = dict(zip(date_key,nos))
	#返回读取结果
	return date_dict