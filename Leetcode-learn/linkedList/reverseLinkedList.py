class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        
        while curr and curr.next:
            tmp = curr.next
            curr.next = curr.next.next 
            tmp.next = None 
            tmp.next = head
            head = tmp
        
        return head
