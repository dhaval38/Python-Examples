def integers():
	i = 1
	while True:
		yield i
		i += 1


def squares():
	for i in integers():
		yield i*i

def take(n, seq):
	result = []
	seq = iter(seq)
	try:
		for i in range(n):
			result.append(seq.next())
	except StopIteration:
		pass

	return result
	
		
