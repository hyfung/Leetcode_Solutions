# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        flatten = []
        grouped = []
        
        ptr = head
        while ptr:
            flatten.append(ptr.val)
            ptr = ptr.next
        
        print(flatten)
        
        while flatten:
            grouped.append(flatten[0:k])
            flatten = flatten[k:]
        
        flatten = []
        
        print(grouped)
        
        for i,v in enumerate(grouped):
            if len(grouped[i]) == k:
                grouped[i] = grouped[i][::-1]
        
        print(grouped)
        
        for l in grouped:
            flatten += l
            
        print(flatten)
        
        head = ListNode(flatten[0])
        ptr = head
        for v in flatten[1:]:
            ptr.next = ListNode(v)
            ptr = ptr.next
            
        return head
