# Lintcode 225: 在链表中找节点  · find node in linked list

# 题目描述: Find a node with given value in a linked list. Return null if not exists.
# 在链表中找值为 value 的节点，如果没有的话，返回空(null)。

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    # @param head: the head of linked list.
    # @param val: an integer
    # @return: a linked node or null
    def findNode(self, head, val):
        # Write your code here
        # 复杂度O(n)
        while head is not None:
            if head.val == val:
                return head
            head = head.next
        return None
