# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        ls = []
        
        def traverse(node):
            nonlocal ls
            
            if node is None:
                return
            traverse(node.left)
            ls.append(node.val)
            traverse(node.right)
        
        traverse(root)
        
        ls.sort()
        
        x = 2147483647
        
        for i in range(len(ls) - 1):
            x = min(abs(ls[i+1]-ls[i]), x)
        
        return x
        
        
