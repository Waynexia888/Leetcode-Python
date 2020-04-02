# Lintcode 219: 在排序链表中插入一个节点  · Insert Node in Sorted Linked List

# 题目描述: Insert a node in a sorted linked list.
#  在链表中插入一个节点。

# 参考资料： https://lumingdong.cn/python-implements-classical-leetcode-algorithm-linked-list.html

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return the head of new linked list
    def insertNode(self, head, val):
        
        # # dummy = ListNode(0, head)
        # dummy = ListNode(0)
        # dummy.next = head
        # pre = dummy

        # while pre.next and pre.next.val < val:
        #     pre = pre.next 
        # node = ListNode(val)
        # node.next = pre.next
        # # node = ListNode(val, p.next)
        # pre.next = node
        # return dummy.next

        dummy = ListNode(0)
        dummy.next = head
        previous, current = dummy, dummy.next

        while current and current.val < val:
            current = current.next
        node = ListNode(val)
        node.next = current
        previous.next = node
        return dummy.next


