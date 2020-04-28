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
    @return: An integer
    """

    def maxDepth(self, root):
        # write your code here
        #时间复杂度： 0（n）
        # 深度对于节点node而言， 高度对于子树而言

        # method 1: 遍历法解决问题的思路
        # 通过前序/中序/后序的某种遍历，游走整棵树，通过一个全局变量或者传递的参数来记录这个过程所遇到的点和需要计算的结果。

        #     self.depth = 0
        #     self.traverse(root, 1)
        #     return self.depth

        # def traverse(self, node, currentDepth):
        #     if node is None:
        #         return

        #     self.depth = max(self.depth, currentDepth)
        #     self.traverse(node.left, currentDepth + 1)
        #     self.traverse(node.right, currentDepth + 1)

        # method 2: 分治法解决问题的思路
        # 先让左右子树去解决同样的问题，然后得到结果之后，再整合为整棵树的结果。

        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1
