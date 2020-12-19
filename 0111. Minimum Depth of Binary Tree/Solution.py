# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        depth = 0
        min_depth = 1000000
        
        def traversal(node):
            nonlocal depth, min_depth
            
            if node is None:
                return
            
            depth += 1
            traversal(node.left)
            
            if node.left is None and node.right is None:
                min_depth = min(depth, min_depth)
            
            traversal(node.right)            
            depth -= 1
            
        
        traversal(root)
        
        return min_depth
