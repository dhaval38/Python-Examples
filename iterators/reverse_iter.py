class reverse:
	def __init__(self, list1):
		self.list1 = list1
		self.i = 1

	def __iter__(self):
		return self

	def next(self):
		if self.i <= len(self.list1):
			item = self.list1[-1*self.i]
			self.i += 1
			return item
		else:
			raise StopIteration

