# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        sum = 0
              
        # Define an in-order traversal function
        def inorder(node):
            nonlocal sum
            if node is None:
                return
            inorder(node.left)
            if node.val >= low and node.val <= high:
                sum = sum + node.val
            inorder(node.right)        
        
        inorder(root)
        
        return sum
        
