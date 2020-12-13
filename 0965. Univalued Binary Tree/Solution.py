# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        const = root.val
        ret = True
        
        def traversal(node):
            nonlocal ret
            if not node:
                return
            traversal(node.left)
            if node.val != const:
                ret = False
            traversal(node.right)
            
            
        traversal(root)
        
        return ret
        
