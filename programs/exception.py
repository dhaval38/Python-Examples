import re
with open("demo.txt", "r") as f:
	data = f.readlines()
	print data
	data = "".join(data)
	print data
	match = re.findall(r'error|exception', data, re.I | re.M)
	print match.count('error')
