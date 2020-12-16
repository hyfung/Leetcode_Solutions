# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.ls = []
        self.cnt = 0
        
        def traverse(self, node):
            if node is None:
                return
            traverse(self, node.left)
            self.ls.append(node.val)
            traverse(self, node.right)
        
        traverse(self, root)
        print(self.ls)
        
        

    def next(self) -> int:
        v = self.ls[self.cnt]
        self.cnt += 1
        return v
        

    def hasNext(self) -> bool:
        return self.cnt != len(self.ls)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
