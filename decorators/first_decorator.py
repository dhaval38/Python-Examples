def strong_decorate(func):
	def func_wrapper(name):
		print "strong_decorate : "+name
		print "<strong> {0}".format(func(name))
		return "<strong>{0}</strong>".format(func(name))
	return func_wrapper

def div_decorate(func):
	def func_wrapper(name):
		print "div_decorate : "+name
		print "<div> {0}".format(func(name))
		return "<div>{0}</div>".format(func(name))
	return func_wrapper

def p_decorate(func):
	def func_wrapper(name):
		print "p_decorate : "+name
		print "<p> {0}".format(func(name))
		return "<p>{0}</p>".format(func(name))
	return func_wrapper

@strong_decorate
@div_decorate
@p_decorate
def get_text(name):
	return "My name is {0}".format(name)

print get_text("Dhaval")

