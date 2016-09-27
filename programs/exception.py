import re
with open("demo.txt", "r") as f:
        cont = f.read()
	data = f.readlines()
	print cont, len(cont), data
	data = "".join(data)
	print data
	match = re.findall(r'error|exception', data, re.I | re.M)
	print match.count('error')
