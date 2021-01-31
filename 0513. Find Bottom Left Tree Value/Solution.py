# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        d = dict()
        
        depth = 0
        def traverse(node):
            nonlocal depth
            
            if node is None:
                return
            
            if depth not in d:
                d[depth] = []
            
            d[depth].append(node.val)
            
            depth += 1
            traverse(node.left)
            
            traverse(node.right)
            depth -= 1
        
        traverse(root)
        # print(d)
        
        return d[max(d.keys())][0]
        
