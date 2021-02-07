# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        flatten_a = []
        flatten_b = []
        target = []
        
        ptr = list1
        while ptr:
            flatten_a += [ptr.val]
            ptr = ptr.next
        
        ptr = list2
        while ptr:
            flatten_b += [ptr.val]
            ptr = ptr.next
        
        target += flatten_a[0:a] + flatten_b + flatten_a[b+1:]
        
        head = ListNode(target[0])
        
        ptr = head
        for i in target[1:]:
            ptr.next = ListNode(i)
            ptr = ptr.next
        
        return head
