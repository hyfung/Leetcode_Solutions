# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
                
        path = []
        curSum = 0
        pathList = []
        
        def traverse(node):
            nonlocal pathList
            if node:
                path.append(node.val)
                # print(node.val)
                if node.left is None and node.right is None:
                    # Leaf node
                    # print(path, sum(path))
                    # curSumList.append(sum(path))
                    if sum(path) == targetSum:
                        pathList.append(list(path)) #Deepcopy
                    # print(curSumList)
            
                traverse(node.left)
                traverse(node.right)
                path.pop()
        
        traverse(root)
        return pathList
