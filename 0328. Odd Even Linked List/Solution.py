# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        flatten_odd = []
        flatten_even = []
        
        is_odd = True
        ptr = head
        while ptr:
            if is_odd:
                flatten_odd += [ptr.val]
                is_odd = False
            else:
                flatten_even += [ptr.val]
                is_odd = True
            ptr = ptr.next
        
        flatten = flatten_odd + flatten_even
        
        head = ListNode(flatten[0])
        ptr = head
        for i in flatten[1:]:
            ptr.next = ListNode(i)
            ptr = ptr.next
            
        return head
        
