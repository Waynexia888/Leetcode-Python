# implement queue by linked list 如何用连表实现队列
# method 1

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

# method 2:


# 定义 LinkedNode

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyQueue:
    def __init__(self):
        self.dummy = ListNode(-1)
        self.tail = self.dummy

    """
    @param: item: An integer
    @return: nothing
    """

    def enqueue(self, item):
        node = ListNode(item)
        self.tail.next = node  # 最后一个元素的next 指向node
        self.tail = node      # 这里做的是： 更新最后一个元素

    """
    @return: An integer
    """

    def dequeue(self):
        item = self.dummy.next.val # 在删除dummy的next元素之前，先把该元素的val记录下来，方便后面return
        self.dummy.next = self.dummy.next.next
        if self.dummy.next is None:
            self.tail = self.dummy # 如果dummy的next 是空，需要重置一下最后一个元素
        return item

    #判断是否为空，这个可写可不写
    def empty(self):
        return self.dummy.next is None

