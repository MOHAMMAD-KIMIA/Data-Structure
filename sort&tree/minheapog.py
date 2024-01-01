class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def get_min(self):
        if len(self.heap) > 0:
            return self.heap[0]
        else:
            return None

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        i = 0
        while self.left_child(i) < len(self.heap):
            child_index = self.left_child(i)
            if self.right_child(i) < len(self.heap) and self.heap[self.right_child(i)] < self.heap[self.left_child(i)]:
                child_index = self.right_child(i)
            if self.heap[i] > self.heap[child_index]:
                self.heap[i], self.heap[child_index] = self.heap[child_index], self.heap[i]
                i = child_index
            else:
                break
        return min_val

    def build_heap(self, input_list):
        self.heap = input_list[:]
        for i in range(len(self.heap) // 2, -1, -1):
            self.min_heapify(i)

    def min_heapify(self, i):
        l = self.left_child(i)
        r = self.right_child(i)
        smallest = i
        if l < len(self.heap) and self.heap[l] < self.heap[smallest]:
            smallest = l
        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest)

    def __len__(self):
        return len(self.heap)


#input_list = [4, 1, 7, 3, 8, 5]
a=MinHeap()
a.insert(4)
a.insert(1)
a.insert(7)
a.insert(3)
a.insert(8)
a.insert(5)
a.build_heap(a.heap)
print(a.heap)
