# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        elif not head.next: return head
        curr = head
        size = 0
        while curr:
            size += 1
            curr = curr.next
            
        curr = head
        k = k % (size) if k > size else k
        if k == 0:
            return head
        k = size - k 
        while k != 1 :
            curr = curr.next
            k -= 1
        
        new_head = curr.next
        curr.next = None
        holder = new_head
        while holder.next:
            holder = holder.next
        
        holder.next = head
        head = new_head
        
        return head
        
        
            
        
