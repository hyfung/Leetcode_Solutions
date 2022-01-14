# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        result = 0
        
        def traverse(node, parent, grandparent):
            nonlocal result
            # Inorder traversal            
            if node is not None:
                # Check if grandparent is even-valued
                if grandparent and grandparent % 2 == 0:
                    result += node.val
                traverse(node.left, node.val, parent)
                traverse(node.right, node.val, parent)

        traverse(root, None, None)
        
        return result
    
