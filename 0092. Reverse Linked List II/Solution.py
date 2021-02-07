# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        flatten = []
        
        ptr = head
        while ptr:
            flatten += [ptr.val]
            ptr = ptr.next
        
        regularized = (flatten[0:m-1] + flatten[m-1:n][::-1] + flatten[n:])
        
        head = ListNode(regularized[0])
        ptr = head
        for i in regularized[1:]:
            ptr.next = ListNode(i)
            ptr = ptr.next
        return head
