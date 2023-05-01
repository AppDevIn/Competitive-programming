# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        end = head
        tmp = None
        index = 1
        if not head:
            return head
        while end.next:
            end = end.next
            index += 1
        index = index // 2
        while index != 0:
            end.next = curr.next
            curr.next = curr.next.next
            
            end = end.next
            end.next = None
            
            
            curr = curr.next if curr.next else curr
            index -= 1
            
        
        return head
            
            
            
        
