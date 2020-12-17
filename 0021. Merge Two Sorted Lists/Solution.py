# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_ptr = l1
        l2_ptr = l2
        
        ls = []
        
        if l1 is None and l2 is None:
            return None
        
        while l1_ptr:
            ls.append(l1_ptr.val)
            l1_ptr = l1_ptr.next
        
        while l2_ptr:
            ls.append(l2_ptr.val)
            l2_ptr = l2_ptr.next
        
        ls.sort()
        
        head = ListNode(ls[0])
        
        ptr = head
        for v in ls[1:]:
            ptr.next = ListNode(val=v)
            ptr = ptr.next
            
        return head
    
        
