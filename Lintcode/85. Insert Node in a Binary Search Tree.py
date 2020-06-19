"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """

    def insertNode(self, root, node):
        # 在树上定位要插入节点的位置。
        # 1. 如果它大于当前根节点，则应该在右子树中，如果没有右子树则将该点作为右儿子插入；若存在右子树则在右子树中继续定位。
        # 2. 如果它小于当前根节点，则应该在左子树中，处理同上。

        if root is None:
            return node

        if root.val > node.val:
            root.left = self.insertNode(root.left, node)
        else:
            root.right = self.insertNode(root.right, node)

        return root
