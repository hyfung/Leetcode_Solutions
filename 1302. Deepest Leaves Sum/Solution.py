# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        
        depth = 0
        level = dict()
        
        # First we traverse the tree and build a dictionary
        def traverse(node):
            nonlocal depth, level
            if node is None:
                return
            
            depth += 1
            traverse(node.left)
            depth -= 1
            
            if depth in level:
                level[depth] += [node.val]
            else:
                level[depth] = [node.val]
            
            depth += 1
            traverse(node.right)
            depth -= 1
        
        traverse(root)
        
        # Simply find the deepest key then take a sum() of its values
        return sum(level[max(level.keys())])
