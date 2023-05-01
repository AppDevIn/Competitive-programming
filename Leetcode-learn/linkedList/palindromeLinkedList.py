class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        text = ""
        
        while head.next:
            text += str(head.val)
            head = head.next
        text += str(head.val)

        return text == text[::-1]
