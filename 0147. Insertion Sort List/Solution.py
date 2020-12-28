# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        
        if head is None:
            return None
        
        ptr = head
        vals = []
        
        while ptr:
            vals.append(ptr.val)
            ptr = ptr.next
            
        vals.sort()
        
        head = ListNode(vals[0])
        
        ptr = head
        
        for v in vals[1:]:
            ptr.next = ListNode(v)
            ptr = ptr.next
        
        return head
        
