# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        stack = []
        bin_nums = []
        def traverse(node):
            nonlocal stack
            
            if node is None:
                return
            
            stack.append(str(node.val))
            
            traverse(node.left)
            
            if node.left is None and node.right is None:
                print(stack)
                bin_nums.append(eval("0b" + "".join(stack)))
            
            
            traverse(node.right)
            
            stack.pop()
        
        traverse(root)
        
        return sum(bin_nums)
            
            
        
