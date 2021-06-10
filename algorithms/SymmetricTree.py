# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invert(self, root: TreeNode):
        tmp = root.right
        root.right = root.left
        root.left = tmp
    def compareInverse(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None and right is not None:
            return False
        elif left is not None and right is None:
            return False
        elif left is None and right is None:
            return True

        if left.val != right.val:
            return False
            
        self.invert(right)
        return self.compareInverse(left.left, right.left) and self.compareInverse(left.right, right.right)
        
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.compareInverse(root.left, root.right)
        

