"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        
        
        queue = []
        queue.append(root)
        prevNode = None
        
        while queue:
            currNode = queue.pop(0)
            # print(f"prevNode: {prevNode.val if prevNode else None}")
            # print(f"currNode: {currNode.val}")
            if prevNode:
                prevNode.next = currNode
            # print(f"---")
            
            prevNode = currNode
            
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)
                
        
        currNode = root
        currNode.next = None
        while currNode.right:
            currNode.right.next = None
            currNode = currNode.right
            
        return root
    
    
