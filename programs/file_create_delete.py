import time
import re
from subprocess import Popen, PIPE

time_milli = lambda:int(round(time.time()*1000))
files = []

def checkUsage():
	cmd = "df -h"
	usedSpace = ""
	res = Popen(cmd, shell=True, stdout=PIPE)
	output = res.communicate()[0]
	output = output.split("\n")
	for item in output:
		if re.search(r'/run$', item, re.I|re.M):
			item = item.split()
			usedSpace = item[4].split("%")
			return int(usedSpace[0])
	
def createFile():
	filename = "/run/file_" + str(time_milli())
	cmd = "dd if=/dev/urandom of=%s bs=1024 count=10000" %filename
	res = Popen(cmd, shell=True)
	output = res.communicate()
	files.append(filename)
	print "\nCreated file : %s" %filename
	#print res, output, files

def deleteFile():
	filename = files[0]
	cmd = "rm -f %s" %filename
	res = Popen(cmd, shell=True)
	output = res.communicate()
	print "\nDelete file : %s, %s" %(filename, files)
	files.pop(0)
	#print res, output, files

if __name__ == "__main__":
	used = checkUsage()
	free = 100-used
	while True:
		if used < 95 and free > 5:
			createFile()
			used = checkUsage()
			free = 100-used
			print "used : %s, free : %s" %(used, free)
		else:
			while free < 25:
				deleteFile()
				used = checkUsage()
				free = 100-used
				print "deleteFile : used : %s, free : %s" %(used, free)
		
