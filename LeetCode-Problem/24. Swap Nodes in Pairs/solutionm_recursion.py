# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case would be head.next empty or .head.next.next empty

        if not head or not head.next: return head

        first_node = head
        secon_node = head.next

        first_node.next = self.swapPairs(head.next.next)
        secon_node.next = head

        return secon_node
        
        

                

