#coding=utf-8
########################################
#filename:test_xlutils.py
#author:defias
#date:2017-11-01
#function:想excel文件中写入数据
#######################################
import xlrd
import xlutils3.copy

# #打开一个workbook
# rb = xlrd.open_workbook('test_xlwt.xls')
# wb = xlutils3.copy.copy(rb)
# #获取sheet对象，通过sheet_by_index()获取的sheet对象没有write()方法
# ws = wb.get_sheet(0)
# #写入数据
# for i in range(50):
# 	ws.write(1,i,'')
# 	ws.write(i,2,'changed! + %s' %i)
# #添加sheet页面
# #wb.add_sheet('工作表3',cell_overwrite_ok=True)
# #利用保存时同名覆盖达到修改excel文件的目的，注意未被修改的内容不变
# wb.save('test_xlwt.xls')

def xlus(date,n):
	rb = xlrd.open_workbook(date)
	wb = xlutils3.copy.copy(rb)

	ws = wb.get_sheet(0)

	for i in range(n):
		ws.write(1,i,'')
		ws.write(i,2,'hello! + %s' %i)
	wb.save(date)

xlus('test_xlwt.xls',30)