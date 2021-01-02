# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        flatten = dict()
        level = 0
        
        # Part 1: Flatten the tree
        def traverse(node):
            nonlocal flatten, level
            
            if node is None:
                return
            
            if level not in flatten:
                flatten[level] = [node.val]
            else:
                flatten[level] += [node.val]
            
            level += 1
            traverse(node.left)
            level -= 1
            
            level += 1
            traverse(node.right)
            level -= 1
            
        traverse(root)
        
        # Part 2: Verify Odd-even
        for i in range(len(flatten)):
            if i % 2 == 0:
                # Even layer
                for j in range(len(flatten[i]) - 1):
                    if flatten[i][j] % 2 == 0:
                        return False
                    # Check strictly increasing
                    if not flatten[i][j+1] > flatten[i][j]:
                        return False
                    
                if flatten[i][-1] % 2 == 0:
                    return False
            else:
                # Odd layer
                for j in range(len(flatten[i]) - 1):
                    if flatten[i][j] % 2 == 1:
                        return False
                    if not flatten[i][j+1] < flatten[i][j]:
                        return False
                if flatten[i][-1] % 2 == 1:
                    return False
            
        return True
        
