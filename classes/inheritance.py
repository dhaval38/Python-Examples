class Pets:
	name = "pet animals"
	
	@classmethod
	def about(cls):
		print("This class is about {}!".format(cls.name))

class Dogs(Pets):
	name = "mans best friend"

class Cats(Pets):
	name = "cats"

if __name__ == "__main__":
	p = Pets()
	p.about()

	d = Dogs()
	d.about()
	
	c = Cats()
	c.about()
