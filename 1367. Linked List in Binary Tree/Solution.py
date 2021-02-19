# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        
        # First we flatten the list
        flatten_list = []
        ptr = head
        while ptr:
            if ptr.val:
                flatten_list.append(ptr.val)
            ptr = ptr.next
        print(flatten_list)
        # End -----------------------

        # Then we perform DFS to obtain the longest path
        found = False
        
        path = []
        paths = []
        def traverse(node):
            nonlocal paths, path
            if node is None:
                return
            
            path.append(node.val)
            
            if node.left is None and node.right is None:
                paths.append(copy.copy(path))
            
            traverse(node.left)
            traverse(node.right)
            
            path.pop()
            
        traverse(root)
        print(paths)
        
        flatten_list_str = ",".join([str(x) for x in flatten_list])
        print(flatten_list_str)
        
        for path in paths:
            path_str = ",".join([str(x) for x in path])
            if flatten_list_str in path_str:
                return True
        return False
            
