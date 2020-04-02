# Lintcode 174: 删除链表中倒数第n个节点  · Remove Nth Node From End of List

# 题目描述: Given a linked list, remove the nth node from the end of 
# list and return its head
# 给定一个链表，删除链表中倒数第n个节点，返回链表的头节点。

# 样例1: 
# Input: list = 1 -> 2 -> 3 -> 4 -> 5 -> null， n = 2
# Output: 1 -> 2 -> 3 -> 5 -> null

# 样例2:
# Input:  list = 5 -> 4 -> 3 -> 2 -> 1 -> null, n = 2
# Output: 5 -> 4 -> 3 -> 1 -> null

# 挑战
# O(n)时间复杂度

# 注意事项
# 链表中的节点个数大于等于n

# 思路视频： https://www.youtube.com/watch?v=8Jq8ikIeF1M


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

        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next
