"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """

    def removeNthFromEnd(self, head, n):
        # write your code here
        # 要有一个头指针，dummy node, 以防删除的点是头
        # 设置快慢指针，快指针先行n步，慢指针之后出发，什么时候快指针指向最后一个点的时候，慢指针指向的点就是待删除点的前一个点。让slow.next = slow.next.next即可
        # dummy -> 1->2->3->4->5->null， n = 2
        #   s
        #             f
        #                s
        #                      f

        if n <= 0:
            return None

        dummy = ListNode(-1, head)
        slow, fast = dummy, dummy

        for i in range(0, n + 1):  # 为什么n + 1?
            if fast is None:     # eg: dummy -> null
                return None
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next
