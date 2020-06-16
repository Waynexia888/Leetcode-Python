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
    @return: the maximum weight node
    """

    def findSubtree(self, root):
        # write your code here
        maximum_subtree_sum, maximum_subtree_root, sum_of_tree = self.getTreeSum(
            root)
        return maximum_subtree_root

    def getTreeSum(self, root):
        if root is None:
            return -1, None, 0

        left_maximum_subtree_sum, left_maximum_subtree_root, left_sum_of_tree = self.getTreeSum(
            root.left)
        right_maximum_subtree_sum, right_maximum_subtree_root, right_sum_of_tree = self.getTreeSum(
            root.right)

        sum_of_tree = left_sum_of_tree + right_sum_of_tree + root.val

        if left_maximum_subtree_sum == max(left_maximum_subtree_sum, right_maximum_subtree_sum, sum_of_tree):
            return left_maximum_subtree_sum, left_maximum_subtree_root, sum_of_tree

        if right_maximum_subtree_sum == max(left_maximum_subtree_sum, right_maximum_subtree_sum, sum_of_tree):
            return right_maximum_subtree_sum, right_maximum_subtree_root, sum_of_tree

        return sum_of_tree, root, sum_of_tree
