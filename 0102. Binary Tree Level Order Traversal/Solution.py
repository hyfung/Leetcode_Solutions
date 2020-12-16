# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        level = 0
        res = []
        for i in range(1024):
            res.append([])
        
        def traversal(node):
            nonlocal res, level
            
            if node is None:
                res.append(None)
                return
            level += 1
            traversal(node.left)
            level -= 1
            
            res[level].append(node.val)
            
            level += 1
            traversal(node.right)
            level -= 1
            
        traversal(root)
        return [x for x in res if x ]
