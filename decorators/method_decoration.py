def p_decorate(func):
	def func_wrapper(*args, **kwargs):
		return "<p>{0}</p>".format(func(*args, **kwargs))

	return func_wrapper

class Person:
	def __init__(self):
		self.name = "Dhaval"
		self.family = "Rajput"

	@p_decorate
	def get_fullname(self):
		return self.name + " " + self.family


person = Person()
print person.get_fullname()
