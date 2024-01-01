class Node:
    def __init__(self, neighbor):
        self.neighbor = neighbor
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addEdge(self, neighbor):
        newNode = Node(neighbor)
        newNode.next = self.head
        self.head = newNode

    def removeEdge(self, neighbor):
        thisNode = self.head
        if thisNode and thisNode.neighbor == neighbor:
            self.head = thisNode.next
            return
        while thisNode.next:
            if thisNode.next.neighbor == neighbor:
                thisNode.next = thisNode.next.next
                return
            thisNode = thisNode.next

    def display(self):
        thisNode = self.head
        while thisNode:
            print(f"{thisNode.neighbor} -> ", end='')
            thisNode = thisNode.next
        print("None")


class Graph:
    def __init__(self):
        self.vertex = {}
        self.size = 0

    def addVertex(self, vertex):
        if vertex not in self.vertex:
            self.vertex[vertex] = LinkedList()
            self.size += 1
            return True
        else:
            return False

    def remove_vertex(self, vertex):
        if vertex not in self.vertex:
            return False
        else:
            del self.vertex[vertex]
            self.size -= 1
            for otherVertex, linkedList in self.vertex.items():
                linkedList.remove_edge(vertex)
            return True

    def addEdge(self, vertex1, vertex2):
        if vertex1 in self.vertex and vertex2 in self.vertex:
            self.vertex[vertex1].addEdge(vertex2)
            self.vertex[vertex2].addEdge(vertex1)
            return True
        else:
            return False

    def removeEdge(self, vertex1, vertex2):
        if vertex1 in self.vertex and vertex2 in self.vertex:
            self.vertex[vertex1].removeEdge(vertex2)
            self.vertex[vertex2].removeEdge(vertex1)
            return True
        else:
            return False

    def DFS(self, start, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)
        print(start, end=' ')

        thisNode = self.vertex[start].head
        while thisNode:
            neighbor = thisNode.neighbor
            if neighbor not in visited:
                self.DFS(neighbor, visited)
            thisNode = thisNode.next


    def display(self):
        for vertex, linkedList in self.vertex.items():
            print(f"Vertex {vertex}: ", end='')
            linkedList.display()

    def BFS(self, start, visited=None):
        if visited == None:
            visited = set()
        queue = []
        queue.append(start)
        visited.add(start)
        while queue:
            s = queue.pop()
            print(s, end=" ")
            thisNode = self.vertex[s].head  # Move this line inside the while loop
            while thisNode:
                neighbor = thisNode.neighbor
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                thisNode = thisNode.next
        print()  # Add a newline after BFS traversal



