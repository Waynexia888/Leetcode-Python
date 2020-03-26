# Binary Tree Leaf Sum
# Given a binary tree, calculate the sum of leaves

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {int} an integer
    def leafSum(self, root):
        # Write your code here
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val
        return self.leafSum(root.left) + self.leafSum(root.right)

    #时间复杂度： o（n）， 因为每个节点仅被遍历一次
