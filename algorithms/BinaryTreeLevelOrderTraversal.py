# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = {}
        if root:
            nodes_queue = [(0, root)]
        else:
            return []

        while len(nodes_queue) > 0:
            node_level, node = nodes_queue.pop(0)
            values = result.get(node_level, [])
            values.append(node.val)
            result[node_level] = values

            if node.left:
                nodes_queue.append((node_level + 1, node.left))
            if node.right:
                nodes_queue.append((node_level + 1, node.right))


        return [values for (_, values) in result.items()]
    
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(6)
root.left.left = TreeNode(1)

print(Solution().levelOrder(root))