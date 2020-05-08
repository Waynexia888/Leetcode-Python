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

    def flatten(self, root):
        # write your code here
        # 分治法：先flatten左边，然后flatten右边， 然后连接起来（参考下面1， 2，3）
        # 1. 左子树的最后一个点（即leaf）连接右子树的第一个点
        # 2. 左子树代替右子树（即root的右边连接左子树的第一个点）
        # 3. 左子树 = None
        self.flatten_and_return_last_node(root)

    # restructure and return last node in preorder
    def flatten_and_return_last_node(self, root):
        if root is None:
            return None

        left_last = self.flatten_and_return_last_node(root.left)
        right_last = self.flatten_and_return_last_node(root.right)

        # connect
        if left_last is not None:
            left_last.right = root.right
            root.right = root.left
            root.left = None

        return right_last or left_last or root  # 返回第一个非空的那个
