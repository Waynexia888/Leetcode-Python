# 打印出一个树的中序遍历
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


    def myPrint(node):
        if node is None:
            return 

        myPrint(node.left)
        print node.val,
        myPrint(node.right)
    
node1 = TreeNode(3)
node2 = TreeNode(1)
node3 = TreeNode(4)
node4 = TreeNode(6)
node5 = TreeNode(7)

node1.left = node2
node1.right = node4

node4.left = node3
node4.right = node5

myPrint(node1)




