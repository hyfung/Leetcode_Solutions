# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        counter = 0
        
        ptr = head
        
        while ptr:
            counter += 1
            ptr = ptr.next
                
        target = counter // 2
        
        ptr = head
        while ptr:
            if target == 0:
                return ptr
            target -= 1
            ptr = ptr.next
        
