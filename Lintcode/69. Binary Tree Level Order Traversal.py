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
    @param root: A Tree
    @return: Level order a list of lists of integer
    """

    def levelOrder(self, root):
        # write your code here
        result = []

        if root is None:
            return result

        #初始化队列，并且把跟节点放入队列
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)

        return result
