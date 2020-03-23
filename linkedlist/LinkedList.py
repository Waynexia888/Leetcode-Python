# -*- coding:utf-8 -*-

class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        # dummy 虚拟的哨兵节点
        self.dummy = ListNode(-1)

    def get(self, location):
        p = self.dummy.next
        for i in range(location):
            p = p.next

        return p.val

    def contains(self, val):
        p = self.dummy.next
        while p is not None:
            if p.val == val:
                return True
            p = p.next

        return False

    def add(self, location, val):
        p = self.dummy
        for i in range(location):
            p = p.next

        node = ListNode(val)
        node.next = p.next
        p.next = node

    def remove(self, location):
        p = self.dummy
        for i in range(location):
            p = p.next

        p.next = p.next.next

    def empty(self):
        return self.dummy.next is None

