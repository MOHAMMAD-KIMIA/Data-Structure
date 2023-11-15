class LQueue:
	def __init__(self, c):
		self.capacity = c
		self.queue = [None for i in range(c)] 
		self.front = self.rear = 0

	def queueisempty(self):
		if(self.rear==self.front):
			return True
		
	def queueisfull(self):
		if(self.rear==self.capacity):
			return True

	def queueEnqueue(self, data):
		if(self.queueisfull()):
			return False
		else:
			self.queue[self.rear] = data
			self.rear = self.rear + 1

	def queuedequeue(self):
		if(self.queueisempty()):
			print("bordanesh zendan")
			return False
		else:
			temp=self.queue[self.front]
			self.queue[self.front]=None
			self.front=(self.front+1) % self.capacity
			return temp
	
	def queuepeek(self):
		return self.queue[self.front]
	
	def reverseQueue(self):
		start = self.front
		end = self.rear - 1
		A = self.queue
		while start < end: 
			A[start], A[end] = A[end], A[start] 
			start += 1
			end -= 1


if __name__ == '__main__':
	q = LQueue(4)
 
    # Print queue elements
	q.queueEnqueue(20)
	q.queueEnqueue(30)
	q.queueEnqueue(10)
	q.queueEnqueue(30)
	q.queueEnqueue(30)
	# q.queueEnqueue(30)
	# q.reverseQueue()
	print("\n")
	a=q.queueisempty()
	b=q.queueisfull()
	#q.queuedequeue()
	print(q.queue)
	print(bool(a))
	print(bool(b))
	