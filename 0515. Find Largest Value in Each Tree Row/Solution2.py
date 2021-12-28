# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        result = []
        
        queue = []
        queue.append((0, root))
        
        d = dict()
        depth = 0
        
        while len(queue) > 0:
            currNode = queue.pop(0)
            
            print(currNode[0], currNode[1].val)
            
            if currNode[0] not in d:
                d[currNode[0]] = currNode[1].val
            else:
                if d[currNode[0]] < currNode[1].val:
                    d[currNode[0]] = currNode[1].val
            
            if currNode[1].left is not None:
                queue.append((currNode[0]+1, currNode[1].left))
                
            if currNode[1].right is not None:
                queue.append((currNode[0]+1, currNode[1].right))
        
        return [x[1] for x in list(d.items())]
        
        
