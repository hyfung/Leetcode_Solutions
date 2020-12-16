# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        
        def traversal(node):
            
            s = set()
            
            if node is None:
                return s
            
            s.add(node.val)
            s = s.union(traversal(node.left))
            s = s.union(traversal(node.right))
            
            return s
        
        s = traversal(root)
    
        if len(s) == 1:
            return -1
        else:
            return sorted(list(s))[1]
        
        
