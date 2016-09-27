# 0, 1, 1, 2, 3, 5, 8, 13, 21 ...
# Recursive fibonacci series
def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2) 

# Generator function for fibonacci series
def fib_gen(n):
	i = 0
	old, new  = 0, 1
	while i < n:
		yield old
		old, new = new, old+new
		i += 1

# Iterative version of fibonacci serie
def fib_iter(n):
	l2 = []
	i, old, new = 0, 0, 1
	while i < n:
		l2.append(old)
		i += 1
		old, new = new, old+new

	return l2

if __name__ == "__main__":
	n = 9
	li = []
	for i in range(n):
		res = fib(i)
		li.append(res)	
	print li

	l1 = fib_gen(n)
	print list(l1)

	print fib_iter(n)	
