# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        import math
        # Get number of nodes by traversing
        
        # Inorder
        N = 0
        def traverse(node):
            nonlocal N
            if node == None:
                return
            traverse(node.left)
            N += 1
            traverse(node.right)
        traverse(root)
        # Using a formula to calculate height
        return math.ceil( (math.log(N+1, 2)) )
        
