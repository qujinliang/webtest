import unittest
from interface_excel import *
class Testcase(unittest.TestCase):
	#测试用例
	def setUp(self):
		pass

	def tearDown(self):
		sheet.close()
	def test_open(self):
		date1 = readexcel_date(0,0,1)
		print(date1)

	def test_open2(self):
		date2 = readexcel_date(0,0,3)
		print(date2)

	def test_open3(self):
		date3 = readexcel_date(0,0,2)
		print(date3)


dd = Testcase()
dd.test_open()
dd.test_open2()
dd.test_open3()