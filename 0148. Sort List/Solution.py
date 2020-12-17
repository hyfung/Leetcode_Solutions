# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        # Grab all elements
        cur_ptr = head
        ls = list()
        while cur_ptr:
            ls.append(cur_ptr.val)
            cur_ptr = cur_ptr.next
            
        ls.sort()
        
        if ls == []:
            return None
        
        # Reconstruct a new list
        head = ListNode(ls[0])
        cur_ptr = head
        for i in ls[1:]:
            cur_ptr.next = ListNode(i)
            cur_ptr = cur_ptr.next
            
        return head
            
        
