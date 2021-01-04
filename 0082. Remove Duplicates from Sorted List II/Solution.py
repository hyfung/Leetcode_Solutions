# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        d = dict()
        
        ptr = head
        
        while ptr:
            if ptr.val not in d:
                d[ptr.val] = 1
            else:
                d[ptr.val] += 1
                
            ptr = ptr.next
        
        vals = [k for k,v in d.items() if v == 1]
        
        if vals == []:
            return None
        
        head = ListNode(vals[0])
        ptr = head
        
        for v in vals[1:]:
            ptr.next = ListNode(v)
            ptr = ptr.next
        
        return head
            
            
