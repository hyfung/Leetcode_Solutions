# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        
        def traverse(node):
            if node is None:
                return
            
            # Perform depth first search
            
            traverse(node.left)
            traverse(node.right)
            
            # Check if node.left is leave
            # Check if node.left is target
            if node.left:
                if node.left.left is None and node.left.right is None:
                    if node.left.val == target:
                        node.left = None
            
            # Check if node.right is leave
            # Check if node.right is target
            if node.right:
                if node.right.left is None and node.right.right is None:
                    if node.right.val == target:
                        node.right = None
        
        # Traverse the tree
        traverse(root)
        
        # If the tree has single node which is the target
        if root.val == target and not root.left and not root.right:
            return None
        
        # Return the chopped tree
        return root
        
