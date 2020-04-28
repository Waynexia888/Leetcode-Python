"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        # write your code here
        # method 1: 分治法
        if root is None:
            return True
        # 在python中 None, False, 空字符串"", 0, 空列表[], 空字典{}, 空元组()都相当于False
        if not self.isBalanced(root.left):
            return False
        if not self.isBalanced(root.right):
            return False

        return abs(self.get_height(root.left) - self.get_height(root.right)) <= 1

    def get_height(self, root):
        if root is None:
            return 0
        left = self.get_height(root.left)
        right = self.get_height(root.right)
        return max(left, right) + 1
