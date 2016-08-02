import multiprocessing

def worker(num):
	''' worker function '''
	print "Worker : ", num
	return

if __name__ == "__main__":
	jobs = []
	for i in range(5):
		p = multiprocessing.Process(target=worker, args=(i,))
		print "Before append"
		jobs.append(p)
		print "jobs ", jobs
		p.start()
	print "After loop"
