"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        
        res = -2147483647
        counter = 0
        
        def traverse(node):
            nonlocal counter, res
            if node is None:
                return
            
            print(node.val, counter)
            
            counter += 1
            res = max(counter, res)
            for c in node.children:
                traverse(c)
            counter -= 1
            
        traverse(root)
        
        return res
        
