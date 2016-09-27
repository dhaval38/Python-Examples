with open("test.txt","w") as f:
	while f.tell() != 1048576:
		f.write("0123") 

with open("test.txt", "r") as f:
	f.seek(-1, 2)
	while f.tell() >= 1048570:
		print f.tell(), f.read(1), f.tell() 
		f.seek(f.tell() - 2)
