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
    @return: a middle node of the linked list
    """

    def middleNode(self, head):
        # 我们将快指针放在第二个节点上，慢指针放在第一个节点上，while
        # 循环中每一次快指针走两步，慢指针走一步。这样当快指针走到头的时候，慢指针就在中点了。
        # 时间复杂度O(n)
        if head is None:
            return None

        slow, fast = head, head.next
        while fast != None and fast.next != None:
            # while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow
