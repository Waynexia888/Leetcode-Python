"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """

    def inorderTraversal(self, root):
        # write your code here
        # method 1:
        #     self.results = []
        #     self.traverse(root)
        #     return self.results

        # def traverse(self, root):
        #     if root is None:
        #         return

        #     self.traverse(root.left)
        #     self.results.append(root.val)
        #     self.traverse(root.right)

        # method 2:
        results = []
        if root is None:
            return []

        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)

        results.extend(left)
        results.append(root.val)
        results.extend(right)

        return results
