"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """

    def findSubtree(self, root):
        # write your code here
        # 纯的divide && conquer 分治法，避免使用全局变量
        # 最小子树的和， 最小子树的根结点，整棵树的和
        # minimum_subtree_sum 有可能在左子树里，或者右子树里， 或者就在整棵二叉树里
        minimum_subtree_sum, minimum_subtree_root, root_sum = self.getTreeSum(
            root)
        return minimum_subtree_root

    def getTreeSum(self, root):
        if root is None:
            return sys.maxsize, None, 0

        left_minimum_subtree_sum, left_minimum_subtree_root, left_sum = self.getTreeSum(
            root.left)
        right_minimum_subtree_sum, right_minimum_subtree_root, right_sum = self.getTreeSum(
            root.right)

        root_sum = left_sum + right_sum + root.val
        # 判断minimum_subtree_sum是否在左子树
        if left_minimum_subtree_sum == min(left_minimum_subtree_sum, right_minimum_subtree_sum, root_sum):
            return left_minimum_subtree_sum, left_minimum_subtree_root, root_sum
        # 判断minimum_subtree_sum是否在右子树
        if right_minimum_subtree_sum == min(left_minimum_subtree_sum, right_minimum_subtree_sum, root_sum):
            return right_minimum_subtree_sum, right_minimum_subtree_root, root_sum
        #如果上述都不是,minimum_subtree_sum就是在整棵二叉树里
        return root_sum, root, root_sum
