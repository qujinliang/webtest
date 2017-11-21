import xlrd
import os


#需求 取第二行以下的数据，然后取每行前13列的数据
data = xlrd.open_workbook('test.xlsx')  #打开xlsx文档
table = data.sheets()[0] #d打印第一张表
nrows = table.nrows      #获取表的行数
for i in range(nrows):   #循环逐行打印
	if i == 0:   #跳过第一行
		continue
	print(table.row_values(i)[:13]) #取前十三列

