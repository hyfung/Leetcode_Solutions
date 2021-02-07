# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        flatten = []
        new_order = []
        ptr = head
        
        while ptr:
            flatten += [ptr.val]
            ptr = ptr.next
        
        print(flatten)
        
        while flatten:
            new_order += [flatten.pop(0)]
            if flatten:
                new_order += [flatten.pop()]
        
        print(new_order)
        
        ptr = head
        for i in new_order[1:]:
            ptr.next = ListNode(i)
            ptr = ptr.next
