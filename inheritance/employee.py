class Person: 
	def __init__(self, first, last, age):
		self.firstname = first
		self.lastname = last
		self.age = age

	def __str__(self):	
		return self.firstname + " " + self.lastname + ", " + str(self.age)


class Employee(Person):
	def __init__(self, first, last, age, staffnumber):
		super().__init__(first, last, age)
		self.staffnumber = staffnumber

	def __str__(self):
		return super().__str__() + ", " + self.staffnumber


if __name__ == "__main__":
	p = Person("Dhaval", "Rajput", 28)
	e = Employee("Paras", "Rajput", 31, "100000")

	print(p)
	print(e)
