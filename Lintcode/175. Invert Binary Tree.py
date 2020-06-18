from collections import deque
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """

    def invertBinaryTree(self, root):
        # 递归的方法
        # if root is None:
        #     return

        # root.left, root.right = root.right, root.left

        # self.invertBinaryTree(root.left)
        # self.invertBinaryTree(root.right)

        # 非递归， 使用宽度优先搜索BFS
        queue = deque([root])

        while queue:
            cur = queue.popleft()

            temp = cur.left
            cur.left = cur.right
            cur.right = temp

            if cur.left is not None:
                queue.append(cur.left)
            if cur.right is not None:
                queue.append(cur.right)
