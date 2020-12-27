# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        
        def traverse(node):
            ls = list()
            
            if node is None:
                return ls
            
            ls += traverse(node.left)
            
            ls += [node.val]
            
            ls += traverse(node.right)
            
            return ls
        
        diff = 2147483647
        
        arr = sorted(traverse(root))
        
        for i in range(len(arr) - 1):
            diff = min(diff, abs(arr[i] - arr[i+1]))
        
        return diff
        
