# Lintcode 165: 合并两个排序链表  · Merge Two Sorted Lists

# 题目描述: Merge two sorted(ascending) linked lists and return it as a 
# new sorted list. The new sorted list should be made by splicing together 
# the nodes of the two lists and sorted in ascending order.
# 将两个排序链表合并为一个新的排序链表

# 样例1:
# 输入: list1 = null, list2 = 0 -> 3 -> 3 -> null
# 输出: 0 -> 3 -> 3 -> null

# 样例2:
# 输入:  list1 = 1 -> 3 -> 8 -> 11 -> 15 -> null, list2 = 2 -> null
# 输出: 1 -> 2 -> 3 -> 8 -> 11 -> 15 -> null

# 两个list不断取较小的头元素，取完以后去掉，直到完全取出一个list。将另一个list直接粘在结尾
# 思路来源： https://www.youtube.com/watch?v=DVv0SqQ0TxM
# 思路来源： https://www.youtube.com/watch?v=Z7VOBq6S5n8

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
    
        dummy = ListNode(0)
        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        if l1:
            current.next = l1
        else: 
            current.next = l2
        
        return dummy.next