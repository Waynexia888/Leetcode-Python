"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum(self, root, target):
        # write your code here
        result = []

        if root is None:
            return []

        if root.left is None and root.right is None and root.val == target:
            path = []
            path.append(root.val)
            result.append(path)
            return result

        leftPaths = self.binaryTreePathSum(root.left, target - root.val)
        rightPaths = self.binaryTreePathSum(root.right, target - root.val)

        for p in leftPaths + rightPaths:
            p.insert(0, root.val)
            result.append(p)

        # for l in leftPaths:
        #     l.insert(0, root.val)
        #     result.append(l)
        # for r in rightPaths:
        #     r.insert(0, root.val)
        #     result.append(r)

        return result
