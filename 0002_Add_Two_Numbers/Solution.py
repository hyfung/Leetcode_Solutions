# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def resolve(ListNode):
            total = ListNode.val
            cnt = 0
            while ListNode.next:
                ListNode = ListNode.next
                cnt += 1
                total += (10 ** cnt) * ListNode.val                
            return total
        
        val = resolve(l1) + resolve(l2)
        print(resolve(l1))
        print(resolve(l2))
        print(val)
        
        cur = None
        prev = None
        for char in str(val):
            prev = cur
            cur = ListNode(int(char), prev) 
            
        return cur
