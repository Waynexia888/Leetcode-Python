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
    @return: Preorder in ArrayList which contains node values.
    """

    def preorderTraversal(self, root):
        # write your code here
        # method 1: use recursion, write helper method

        #     self.results = []
        #     self.traverse(root)
        #     return self.results

        # def traverse(self, root):
        #     if not root:
        #         return

        #     self.results.append(root.val)
        #     self.traverse(root.left)
        #     self.traverse(root.right)

        # method 2: write recursion without helper method, [divide conquer]
        # results = []
        # if not root:
        #     return results

        # left = self.preorderTraversal(root.left)
        # right = self.preorderTraversal(root.right)

        # results.append(root.val)
        # results.extend(left)
        # results.extend(right)

        # return results

        # method 3: without recursion, using stack or queue
        # 1. 首先把root入栈
        # 2. 出栈的元素同时放进结果队列
        # 3. 先把右儿子节点入栈，再把左儿子节点入栈，这样出栈的顺序是先左后右（根节点已出）
        # 4. 按照这个次序继续，直到stack为空
        if root is None:
            return []

        stack = [root]
        results = []

        while stack:
            node = stack.pop()
            results.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return results
