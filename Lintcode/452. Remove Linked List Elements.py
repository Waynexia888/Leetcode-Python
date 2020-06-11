"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: a ListNode
    @param val: An integer
    @return: a ListNode
    """

    def removeElements(self, head, val):
        # write your code here
        dummy = ListNode(-1, head)
        head = dummy

        while head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next

        return dummy.next
