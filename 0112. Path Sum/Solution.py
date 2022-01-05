# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        path = []
        curSum = 0
        curSumList = []
        curSumSet = set()
        
        def traverse(node):
            if node:
                path.append(node.val)
                # print(node.val)
                if node.left is None and node.right is None:
                    # Leaf node
                    # print(path)
                    # curSumList.append(sum(path))
                    curSumSet.add(sum(path))
                    # print(curSumList)
            
                traverse(node.left)
                traverse(node.right)
                path.pop()
        
        traverse(root)
        return targetSum in curSumSet
