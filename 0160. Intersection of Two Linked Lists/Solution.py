# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        occurence = set()
        
        aPtr = headA
        bPtr = headB
        
        while aPtr:
            occurence.add(id(aPtr))
            aPtr = aPtr.next
        
        while bPtr:
            if id(bPtr) in occurence:
                return bPtr
            bPtr = bPtr.next
        
        return None
