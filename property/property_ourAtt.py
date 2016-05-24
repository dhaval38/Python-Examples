class test:
	def __init__(self, x):
		self.ourAtt = x

	@property
	def ourAtt(self):
		return self.__ourAtt

	@ourAtt.setter
	def ourAtt(self, val):
		if val < 0:
			self.__ourAtt = 0
		elif val > 1000:
			self.__ourAtt = 1000
		else:
			self.__ourAtt = val

if __name__ == "__main__":
	t = test(-9)
	print("Val of t.ourAtt : %s" %t.ourAtt)
