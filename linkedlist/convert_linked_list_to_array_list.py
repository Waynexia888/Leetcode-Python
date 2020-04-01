# Lintcode 483: 链表转数组  · Convert a linked list to an array list.

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param {ListNode} head the first node of the linked list.
    @return {int[]} an integer list
    """

    def toArrayList(self, head):
        # Write your code here
        # 遍历链表，并将每个节点的val存储在数组中
        arrList = []
        while head is not None:
            arrList.append(head.val)
            head = head.next
        return arrList

