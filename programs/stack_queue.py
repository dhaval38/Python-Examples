def stack():
	stack = ["a", "b", "c", "d"]
	stack.append("e")
	stack.append("f")
	print stack
	stack.pop()
	stack.pop()
	print stack

def queue():
	queue = ["a", "b", "c", "d"]
	queue.insert(len(queue), "e")
	queue.insert(len(queue), "f")
	print queue
	queue.insert(len(queue), "g")
	print queue
	queue.remove("a")
	queue.remove("b")
	print queue

if __name__ == "__main__":
	stack()
	queue()
