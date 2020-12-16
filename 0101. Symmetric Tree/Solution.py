# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        # Pre order == Post order
        pre = []
        post = []
        def pre_order(node):
            nonlocal pre
            if node is None:
                pre.append(None)
                return
            pre.append(node.val)
            pre_order(node.left)
            pre_order(node.right)
            
        def post_order(node):
            nonlocal post
            if node is None:
                post.append(None)
                return
            post_order(node.left)
            post_order(node.right)
            post.append(node.val)
            
        pre_order(root)
        post_order(root)
        
        return pre == post[::-1]
        
        
