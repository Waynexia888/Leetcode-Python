"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """

    def mergeTwoLists(self, l1, l2):
        # write your code here
        # 两个list不断取较小的头元素，取完以后去掉，直到完全取出一个list。将另一个list直接粘在结尾
        # 思路来源： https://www.youtube.com/watch?v=DVv0SqQ0TxM

        dummy = ListNode(0)
        tail = dummy

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        if l1 is not None:
            tail.next = l1
        else:
            tail.next = l2

        return dummy.next
