import multiprocessing
import time

def slow_worker():
	print 'Starting Worker'
	time.sleep(0.1)
	print 'Exiting Worker'


if __name__ == '__main__':
	p = multiprocessing.Process(target=slow_worker)
	print 'Before : ', p, p.is_alive()	
	
	p.start()
	print 'DURING : ', p, p.is_alive()	

	p.terminate()
	print 'TERMINATED : ', p, p.is_alive()	

	p.join()
	print 'JOINED : ', p, p.is_alive()


