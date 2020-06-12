class Node:
    def __init__(self, _val):
        self.val = _val
        self.next = None


class MyQueue:
    """
    @param: item: An integer
    @return: nothing
    """

    def __init__(self):
        self.head, self.tail = None, None

    def enqueue(self, item):
        # write your code here
        if self.head == None:
            self.tail = Node(item)
            self.head = self.tail
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

    """
    @return: An integer
    """

    def dequeue(self):
        # write your code here
        if self.head == None:
            return -1
        else:
            temp = self.head.val
            self.head = self.head.next
            return temp
