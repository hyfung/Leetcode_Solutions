"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        output = []
        
        def traversal(node):
            if not node:
                return
            output.append(node.val)
            for children in node.children:
                traversal(children)
        
        traversal(root)
        return output
