# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ls = list()
        
        ptr = head
        while ptr:
            ls.append(str(ptr.val))
            ptr = ptr.next
        
        return eval("0b" + "".join(ls))
        
