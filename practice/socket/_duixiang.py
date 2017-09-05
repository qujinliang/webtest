class people(object):
	"""docstring for people"""

	name = ''
	age = 0
	__weight = 0
	def __init__(self, n,a,w):
		self.name = n
		self.age = a
		self.__weight = w
	def speak(self):
		print("%s说：我 %d 岁" %(self.name,self.age))

class student(people):
	"""docstring for student"""
	def __init__(self, n,a,w,g):
		people.__init__(self,n,a,w)
		self.grade = g

	def speak(self):
		print("%s说：我 %d 岁了，我在读%d年级"%(self.name,self.age,self.grade))


s = student('tken',10,60,3)
s.speak()		


