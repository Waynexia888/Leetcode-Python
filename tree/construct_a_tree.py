class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __str__(self):
        return "{val: %s, left: %s, right: %s}" % (self.val. self.left, self.right)
    

"""
    1
2       3
"""
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)

node1.left = node2
node1.right = node3

print node1
print node2
print node3