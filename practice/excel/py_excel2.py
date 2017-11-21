#coding=utf-8
#####################################
#filename:py_excel2.py
#author:defias
#date:2017-10-26
#fuction:读excel文件中的数据
#####################################

import os
import xlrd

print(os.getcwd())
#打开一个workbook
workbook = xlrd.open_workbook('testdata.xlsx')
#抓取所有sheet页的名称
worksheets = workbook.sheet_names()
print('worksheets is %s' %worksheets)
#定位到sheet1
workseet1 = workbook.sheet_by_name(u'工作表1')
"""
#通过索引顺序获取
worksheet1 = workbook.sheet_names()[0]
#或
worksheet1 = workbook.sheet_by_index(0)
"""
"""
#遍历所有sheet对象
for worksheet_name in worksheets:
	worksheet = worksheet.sheet_by_name(worksheet_name)
"""
#遍历工作表1中所有行row, .nrows(返回行数)
num_rows = workseet1.nrows
print (num_rows)
for curr_row in range(num_rows):
	row = workseet1.row_values(curr_row)
	print('row%s is %s' %(curr_row,row))
#遍历工作表1中的所欲列col，.ncols(返回列数)
num_cols = workseet1.ncols
for curr_col in range(num_cols):
	col = workseet1.col_values(curr_col)
	print ('col%s is %s' %(curr_col,col))
#遍历工作表1中的所有单元格cell，现循环行，再循环列
for rown in range(num_rows):
	for coln in range(num_cols):
		cell = workseet1.cell_value(rown,coln)
		print (cell,end=' ')
	print('')
"""
#其他写法
cell = worksheet1.cell(rown,coln).cell_value
print(cell)
#或
cell = worksheet1.row(rown)[coln].value
print(cell)
#或
cell = worksheet1.col(coln)[rown].value
#获取单元格中值得类型，类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
cell_type = worksheet1.cell_type(rown,coln)
print (cell_type)
"""