# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        vals = []
        
        for link_list in lists:
            ptr = link_list
            while ptr:
                vals.append(ptr.val)
                ptr = ptr.next
        
        vals.sort()
        
        if vals == []:
            return None
        
        head = ListNode(vals[0])
        ptr = head
        for v in vals[1:]:
            ptr.next = ListNode(v)
            ptr = ptr.next
        
        return head
