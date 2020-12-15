"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        output = []
        
        def traversal(node):
            if not node:
                return
            for children in node.children:
                traversal(children)
            output.append(node.val)
        
        traversal(root)
        return output
