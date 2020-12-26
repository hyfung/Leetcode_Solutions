# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        leaf_1 = list()
        leaf_2 = list()
        
        def traverse(node):
            ls = list()
            
            if node is None:
                return ls
            
            ls += traverse(node.left)
            
            if node.left is None and node.right is None:
                ls.append(node.val)
            
            ls += traverse(node.right)
            
            return ls
        
        return traverse(root1) == traverse(root2)
        
