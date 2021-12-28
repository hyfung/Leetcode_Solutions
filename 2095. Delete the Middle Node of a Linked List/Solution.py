# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        
        numberOfNode = 0
        ptr = head
        
        while ptr:
            print(f"{numberOfNode}:{ptr.val}")
            ptr = ptr.next
            numberOfNode += 1
        
        ptr = head
        middleIndex = numberOfNode // 2
        
        
        for i in range(0, middleIndex-1):
            ptr = ptr.next
        
        if ptr.next is not None:
            ptr.next = ptr.next.next
        
        return head
        
