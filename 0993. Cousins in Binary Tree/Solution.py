# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        depth = 0
        x_depth = 0
        y_depth = 0
        x_parent = None
        y_parent = None
        isCousin = True
        
        def traverse(node):
            nonlocal depth, x_depth, y_depth, isCousin
            if node is None:
                return
            
            if node.left is not None and node.right is not None:
                if node.left.val is x and node.right.val is y or node.left.val is y and node.right.val is x:
                    isCousin = False
            
            depth += 1
            traverse(node.left)
            depth -= 1
            
            if node.val == x:
                x_depth = depth
            
            if node.val == y:
                y_depth = depth
            
            depth += 1
            traverse(node.right)
            depth -= 1
        
        traverse(root)
        
        return isCousin and x_depth == y_depth
