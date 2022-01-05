# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        if root is None:
            return
        
        vals = []
        
        def inorderTraverse(node):
            vals.append(node.val)
            # print(node.val)
            if node.left:
                inorderTraverse(node.left)
            if node.right:
                inorderTraverse(node.right)
        
        inorderTraverse(root)
        
        # print(vals)
        
        currNode = root
        vals.pop(0)
        while vals:
            currNode.left = None
            currNode.right = TreeNode(vals.pop(0))
            currNode = currNode.right
        
