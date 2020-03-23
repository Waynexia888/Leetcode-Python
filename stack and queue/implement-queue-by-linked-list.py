class MyQueue(object):

    def __init__(self):
        # do some intialize if necessary
        self.first, self.last = None, None

    # @param {int} item an integer
    # @return nothing
    def enqueue(self, item):
        # Write yout code here
        if self.first is None:
            self.first = Node(item)
            self.last = self.first
        else:
            self.last.next = Node(item)
            self.last = self.last.next

    # @return an integer
    def dequeue(self):
        # Write your code here
        if self.first is not None:
            item = self.first.val
            self.first = self.first.next
            return item

        return -1000

class Node():

    def __init__(self, _val):
        self.next = None
        self.val = _val

