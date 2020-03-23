class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
 
class Queue:
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None
 
    def enqueue(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.count += 1
 
    def dequeue(self):
        if self.head is None: # or self.count == 0 or se.f.is_empty()
            raise Exception('This is a empty queue')
        cur = self.head
        self.head = cur.next
        self.count -= 1
        return cur.value
 
    def is_empty(self):
        return self.head is None # or self.count == 0
 
    def size(self):
        return self.count


queue = Queue()
queue.enqueue(10)
queue.enqueue(True)
queue.enqueue('jiuzhang')
print queue.dequeue()
print queue.is_empty()
print queue.size()
print queue.dequeue()
print queue.dequeue()
print queue.is_empty()
print queue.size()

