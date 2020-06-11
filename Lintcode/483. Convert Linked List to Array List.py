"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: the head of linked list.
    @return: An integer list
    """

    def toArrayList(self, head):
        # write your code here
        result = []
        while head is not None:
            result.append(head.val)
            head = head.next

        return result
