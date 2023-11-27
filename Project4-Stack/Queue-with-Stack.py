class QueueViaStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def enQueue(self,x):
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1 [-1])
            self.stack1.pop()
        
        self.stack1.append(x)
        
        while len(self.stack2) != 0:
            self.stack1.append(self.stack2 [-1])
            self.stack2.pop()
            
    def deQueue(self):
        if len(self.stack1) == 0:
            return -1
        x = self.stack1[-1]
        self.stack1.pop()
        return x