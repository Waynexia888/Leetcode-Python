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
    @param level: the depth of the target level
    @return: An integer
    """

    def levelSum(self, root, level):
        # write your code here
        arr = []
        self.helper(root, 1, arr, level)
        return sum(arr)

    def helper(self, root, depth, arr, level):
        if root is None:
            return

        if depth == level:
            arr.append(root.val)
            return

        self.helper(root.left, depth + 1, arr, level)
        self.helper(root.right, depth + 1, arr, level)
