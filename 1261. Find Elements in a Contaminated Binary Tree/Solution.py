# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.root = root
        self.root.val = 0
        self.hashmap = set()
        
        def traversal(node):
            if node is None:
                return
            if node.left is not None:
                node.left.val = node.val * 2 + 1
                self.hashmap.add(node.left.val)
            if node.right is not None:
                node.right.val = node.val * 2 + 2
                self.hashmap.add(node.right.val)
            
            traversal(node.left)
            traversal(node.right)
        
        traversal(self.root)

    def find(self, target: int) -> bool:
#         found = False
        
#         def traversal_1(node):
#             nonlocal found
#             if node is None:
#                 return

#             if node.val == target:
#                 found = True
            
#             traversal_1(node.left)
#             traversal_1(node.right)
        
#         traversal_1(self.root)
        
        return target in self.hashmap
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
