class JiSuan(object):
	"""docstring for Qiuhe"""
	def __init__(self, n=None):
		self.n=[]

	def qiuhe(self,num1,num2):
		num1 = num1
		num2 = num2

		sum = float(num1) + float(num2)

		print("数字{0} 和 {1} 相加结果为： {2}".format(num1,num2,sum))

if __name__ == '__main__':
	js = JiSuan()
	js.qiuhe(3,8)

		
		