#coding=utf-8
###############################################
#filename:test_xlwt.py
#author:defias
#date:xxxx-xx-xx
#function:新建excel文件并写入数据
###############################################

import xlwt
import xlrd
#创建workbook 和 sheet对象 
#workbook = xlwt.Workbook() #注意Workbook的开头W要大写
# sheet1 = workbook.add_sheet('工作表1',cell_overwrite_ok=True)
# sheet2 = workbook.add_sheet('工作表2',cell_overwrite_ok=True)
workbook = xlrd.open_workbook('test_xlwt.xls')
worksheets = workbook.sheet_names()
print('worksheets is %s' %worksheets)

worksheet1 = workbook.sheet_by_name(u'工作表1')

#向sheet页中写入数据
worksheet1.write(0,0,'this should overwrite1')
worksheet1.write(0,1,'aaaaaaaaaaaaa')
worksheet1.write(0,0,'this should overwrite2')
worksheet1.write(1,2,'bbbbbbbbbbbbb')

"""
#----------------使用样式----------------------
#初始化样式
style = xlwt.XFStyle()
#为样式创建字体
font = xlwt.Font()
font.name = 'Times New Roman'
font.bold = True
#设置样式的字体
style.font = font
#使用样式
sheet.write(0,1,'some bold Times text',style)
"""
#保存该excel文件，有同名文件时直接覆盖
workbook.save('test_xlwt.xls')
print('创建excel文件完成！')