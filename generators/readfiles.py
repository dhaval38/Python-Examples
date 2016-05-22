def readfiles(filenames):
	for f in filenames:
		for line in open(f):
			yield line

def grep(pattern, lines):
	return(line for line in lines if pattern in line)

def printlines(lines):
	for line in lines:
		print line,


