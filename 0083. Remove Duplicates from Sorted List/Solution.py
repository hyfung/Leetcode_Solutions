# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if head is None:
            return None
        
        ptr = head
        myset = set()
        
        while ptr:
            myset.add(ptr.val)
            ptr = ptr.next
        
        ptr = None
        
        ls = sorted(list(myset))
        
        head = ListNode(ls[0])
        ptr = head
        
        for i,v in enumerate(ls[1:]):
            ptr.next = ListNode(v)
            ptr = ptr.next
            
        return head
        
        
