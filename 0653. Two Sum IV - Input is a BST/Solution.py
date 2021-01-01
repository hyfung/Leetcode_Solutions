# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        
        s = set()
        
        def flatten(node):
            if node is None:
                return
            
            s.add(node.val)
            flatten(node.left)
            flatten(node.right)
        
        flatten(root)
        
        if len(s) < 2:
            return False
        
        for i in s:
            if (k-i) in s and k != 2*i:
                return True
            
        return False
        
