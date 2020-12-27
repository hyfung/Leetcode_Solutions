# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        ls = list()
        
        def traverse(node):
            nonlocal ls
            
            if node is None:
                return           
            
            traverse(node.left)
            
            ls.append(node.val)
            
            traverse(node.right)
        
        traverse(root)
        
        # Check if ls is strictly increasing
        
        for i in range(len(ls) - 1):
            if ls[i+1] <= ls[i]:
                return False
        
        return True
        
        
