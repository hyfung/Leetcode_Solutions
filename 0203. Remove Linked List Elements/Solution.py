# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        vals = []
        
        cur_ptr = head
        
        while cur_ptr:
            vals.append(cur_ptr.val)
            cur_ptr = cur_ptr.next
        
        vals = [x for x in vals if x != val]
        
        if not vals:
            return None
        
        head = ListNode(vals[0])
        cur_ptr = head
        
        if vals[1:]:
            for val in vals[1:]:
                cur_ptr.next = ListNode(val)
                cur_ptr = cur_ptr.next
        
        return head
