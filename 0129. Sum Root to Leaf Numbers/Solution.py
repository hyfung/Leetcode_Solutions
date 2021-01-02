# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        import copy
        stack = []
        numbers = []
        
        def traverse(node):
            nonlocal stack, numbers
            
            if node is None:
                return
            
            stack.append(node.val)
            print(stack)
            
            if node.left is None and node.right is None:
                numbers.append(copy.copy(stack))
                
            traverse(node.left)
            stack.pop()
            
            stack.append(node.val)
            traverse(node.right)
            stack.pop()
        
        traverse(root)
        print(numbers)
        
        sum = 0
        for number in numbers:
            sum += int("".join([str(ch) for ch in number]))
        return sum
