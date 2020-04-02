# Lintcode 452: 删除链表中的元素  · Remove Linked List Elements

# 题目描述: Remove all elements from a linked list of integers that have value val.
# 删除链表中等于给定值 val 的所有节点。

# 样例 1：
# 输入：head = 1->2->3->3->4->5->3->null, val = 3
# 输出：1 -> 2 -> 4 -> 5 -> null

# 样例 2: 
# 输入：head = 1->1->null, val = 1
# 输出：null

# 参考资料： https://www.youtube.com/watch?v=nwXxL2KtV1Y

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
        dummy = ListNode(0)
        dummy.next = head
        previous, current = dummy, dummy.next

        while current:
            if current.val == val:
                previous.next = current.next
            else:
                previous = current
                # previous = previous.next
            current = current.next

        return dummy.next


