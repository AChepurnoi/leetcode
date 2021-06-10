# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode, max_val=None, min_val=None) -> bool:
        if root is None:
            return True
        if max_val and root.val > max_val:
                return False
        if min_val and root.val < min_val:
                return False

        if root.left:
            if root.val <= root.left.val:
                return False

            if not self.isValidBST(root.left, max_val=max(root.val, max_val) if max_val else root.val, min_val=min_val):
                return False
        if root.right:
            if root.val >= root.right.val:
                return False

            if not self.isValidBST(root.right, min_val=min(root.val, min_val) if min_val else root.val, max_val=max_val):
                return False
            
        return True


