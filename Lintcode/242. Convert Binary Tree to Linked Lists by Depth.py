from collections import deque
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        result = []

        if root is None:
            return result

        queue = deque([root])
        while queue:
            dummy = ListNode(-1)
            temp = dummy

            for _ in range(len(queue)):
                node = queue.popleft()
                temp.next = ListNode(node.val)
                temp = temp.next

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(dummy.next)

        return result
