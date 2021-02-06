# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import statistics
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        
        hashmap = dict()
        level = 0
        
        def traverse(node):
            nonlocal level, hashmap
            if node is None:
                return 
            
            level += 1
            traverse(node.left)
            level -= 1
            
            if level in hashmap:
                hashmap[level] += [node.val]
            else:
                hashmap[level] = [node.val]
            
            level += 1
            traverse(node.right)
            level -= 1
        
        traverse(root)
        
        ret = [0] * (max(hashmap.keys()) + 1)
        
        for k,v in hashmap.items():
            ret[k] = statistics.mean(v)

        return ret
        
