class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next or not head.next.next:
            return False
        
        pointer1 = head.next
        pointer2 = head.next.next
        
        while pointer1.next and pointer2.next and pointer2.next.next:
            if pointer1.val == pointer2.val and pointer1.next == pointer2.next:
                return True
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next
            
        return pointer1.val == pointer2.val and pointer1.next == pointer2.next
            
        
