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
        hashmap = dict()
        
        while ptr:
            if ptr.val not in hashmap:
                hashmap[ptr.val] = 1
            else:
                hashmap[ptr.val] += 1
            ptr = ptr.next
        
        ptr = None
        
        ls = [k for k,v in hashmap.items() if v == 1]
        
        head = ListNode(ls[0])
        ptr = head
        
        for i,v in enumerate(ls[1:]):
            ptr.next = ListNode(v)
            ptr = ptr.next
            
        return head
        
        
