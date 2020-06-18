"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of the binary tree
    @return: An integer
    """

    def leafSum(self, root):
        # write your code here
        arr = []
        self.helper(root, arr)
        return sum(arr)

    def helper(self, root, arr):
        if root is None:
            return

        if root.left is None and root.right is None:
            arr.append(root.val)
            return

        self.helper(root.left, arr)
        self.helper(root.right, arr)
