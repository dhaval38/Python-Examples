class P:
	def __init__(self, x):
		self.x = x

	@property
	def x(self):
		return self.__x

	@x.setter
	def x(self, x):
		print("value of x : %s" %x)
		if x > 1000:
			self.__x = 1000
		elif x < 0:
			self.__x = 0
		else:
			self.__x = x

if __name__ == "__main__":
	p = P(1001)
	print("p.x : %d" %p.x)
	p.x = -2
	print("p.x : %d" %p.x)
	
