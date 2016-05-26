from functools import reduce
numbers = [47, 112, 3, 67, 0, 89]
f = lambda a,b: a if a>b else b
max = reduce(f, numbers)
print max

sum = reduce(lambda x,y: x+y, range(1, 101))
print sum
