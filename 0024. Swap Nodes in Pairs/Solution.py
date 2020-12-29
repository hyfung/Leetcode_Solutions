# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        ls = list()
        
        ptr = head
        while ptr:
            ls.append(ptr)
            ptr = ptr.next
        
        for i in range(len(ls)//2):
            tmp = ls[2*i]
            ls[2*i] = ls[2*i+1]
            ls[2*i+1] = tmp
            
            ls[2*i].next = None
            ls[2*i+1].next = None
        
        for i in range(len(ls) - 1):
            ls[i].next = ls[i+1]
        
        return ls[0]
        
