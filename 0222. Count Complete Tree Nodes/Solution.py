# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # ptr = root
        cnt = 0
        
        def traverse(node):
            nonlocal cnt
            if node is None:
                return
            cnt += 1
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        return cnt
