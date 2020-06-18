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
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        # 分治法思想：
        # 判断左子树是不是BST
        # 判断右子树是不是BST
        # 左子树的最大值 < root.val < 右子树的最小值

        return self.helper(root, -float('inf'), float('inf'))

    def helper(self, root, leftMax, rightMin):
        if root is None:
            return True

        if root.val <= leftMax or root.val >= rightMin:
            return False

        return self.helper(root.left, leftMax, root.val) and self.helper(root.right, root.val, rightMin)
