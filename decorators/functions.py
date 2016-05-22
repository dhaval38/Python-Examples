def compose_greet_msg(name):
	def get_message():
		return "Hello there " + name

	return get_message

greet = compose_greet_msg("Dhaval")
print greet()
