from linkedlist import linkedList

class Queue:
    queue = linkedList.LinkedList()
    
    def enqueue(self, data):
        self.queue.insertAtend(data)
            
    def dequeue(self):
        return self.queue.deleteFromfirst()
        
    def peek(self):
        return self.queue.head.data
    
    def size(self):
        return self.queue.sizeOf()
            
    def display(self):
        self.queue.display()
