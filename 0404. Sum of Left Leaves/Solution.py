# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        ret = 0
        
        def traverse(node, isLeft):
            nonlocal ret
            if node is None:
                return
            
            traverse(node.left, True)
            
            if node.left is None and node.right is None and isLeft:
                ret += node.val
            
            traverse(node.right, False)
        
        traverse(root, False)
        return ret
        
