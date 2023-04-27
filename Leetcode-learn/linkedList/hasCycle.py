class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next
        
        while fast and fast.next:
            if slow.next == fast.next:
                return True
            slow = slow.next
            fast = fast.next.next
            
        return False   


            
        
