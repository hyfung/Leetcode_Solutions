# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        ls = []
        freq = dict()
        
        def traverse(node):
            nonlocal ls
            if node is None:
                return
            ls.append(node.val)
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        
        if ls == []:
            return []
        
        for i in ls:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        ret_ls = []
        mode = max(freq.values())
        for k,v in freq.items():
            if v == mode:
                ret_ls.append(k)
        
        return ret_ls
            