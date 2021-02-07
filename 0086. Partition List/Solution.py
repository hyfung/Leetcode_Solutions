# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head is None:
            return None
        
        flatten = []
        
        ptr = head
        while ptr:
            flatten += [ptr.val]
            ptr = ptr.next
        
        flatten = [i for i in flatten if i < x] + [i for i in flatten if i >= x]

        head = ListNode(flatten[0])
        ptr = head
        for i in flatten[1:]:
            ptr.next = ListNode(i)
            ptr = ptr.next
        
        return head
