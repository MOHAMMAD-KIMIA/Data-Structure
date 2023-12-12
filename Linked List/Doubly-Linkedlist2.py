class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data

class DoubleyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def insertatbegin(self, new_data):
        new_node = Node(data=new_data)
        new_node.next = self.head
        new_node.prev = None
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    
    def insertatend(self, new_data):
        new_node = Node(data=new_data)
        last = self.head
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        while (last.next is not None):
            last = last.next
        last.next = new_node
        new_node.prev = last


    def insertWherever(self, data, pos):
        newNode = Node(data)
        thisNode = self.head
        position = 0
        while thisNode and position < pos:
            prev = thisNode
            thisNode = thisNode.next
            position += 1

        if (pos == 0):
            self.insertatbegin()
        elif (pos == self.list_size()):
            self.insertatend()
        elif (position < pos):
            return False
        else:
            thisNode.prev = newNode
            newNode.next = thisNode
            newNode.prev = prev
            prev.next = newNode

    def RemoveNodeAtBegin(self):
        if(self.head!=None):
            temp=self.head
            self.head=self.head.next 
            temp=None 
            if(self.head!=None):
                self.head.prev=None 

    def deleteFromlast(self):
        if self.head == None:
            return self.data
        thisNode = self.head
        while thisNode.next.next is not None:
            thisNode = thisNode.next
        thisNode.next = None

    def deletWherever(self, pos):
        position = 0
        thisNode = self.head
        
        if self.head == None:
            return False
        
        elif position == pos:
            self.RemoveNodeAtBegin()
        
        else:
            while thisNode is not None and position+1 is not pos:
                position = position + 1
                thisNode = thisNode.next
            
            if thisNode is not None:
                thisNode.next = thisNode.next.next
            
            else:
                return self.data

    def SizeOfList(self): 
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if cur == None:
                break

        return count
    
    def invert(self):
        temp=None
        current=self.head
        while current is not None:
            temp=current.prev
            current.prev=current.next
            current.next=temp
            current=current.prev
        if temp is not None:
            self.head=temp.prev


    def update(self, data, pos):
        thisnode=self.head
        p=0
        if self.head == None:
            return False
        else:
            while thisnode is not None and p+1 is not pos:
                p=p+1
                thisnode=thisnode.next
            if thisnode is not None:
                thisnode=thisnode.next
                thisnode.data=data


    def concat(self,list1,list2):
        thisnode=self.head
        while thisnode.next is not None:
            thisnode=thisnode.next
            
    def display(self, node):
        while(node is not None):
            print(node.data, end=' ')
            node = node.next