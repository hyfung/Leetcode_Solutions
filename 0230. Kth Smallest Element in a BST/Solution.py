# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ls = list()
        
        def traverse(node):
            nonlocal ls
            if node is None:
                return
            
            ls.append(node.val)
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        
        return sorted(ls)[k-1]
        
