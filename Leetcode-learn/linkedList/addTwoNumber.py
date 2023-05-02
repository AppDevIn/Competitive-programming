# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head = ListNode()
        
        remainder = 0
        while l1 or l2 or remainder == 1:
            total = 0 + remainder
            remainder = 0
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
        
            remainder = 1 if total >= 10 else 0
            total = total if total < 10 else total - 10
        
         
            curr.next = ListNode(total)
            curr = curr.next
        return head.next
            
            
