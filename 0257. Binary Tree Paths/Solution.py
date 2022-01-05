# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = []
        pathList = []
        curSumSet = set()
        
        def traverse(node):
            nonlocal pathList
            if node:
                path.append(node.val)
                # print(node.val)
                if node.left is None and node.right is None:
                    pathList.append(list([str(x) for x in path]))
                traverse(node.left)
                traverse(node.right)
                path.pop()
        
        traverse(root)
        # print(pathList)
        
        return ["->".join(x) for x in pathList]
        
