class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        
        while list1 and list2:
            value = 0
            if list1.val > list2.val:
                value = list2.val
                list2 = list2.next 
            else:
                value = list1.val
                list1 = list1.next
                
            curr.next = ListNode(value)
            curr = curr.next

        if list2 or list1:
            curr.next = list2 if list2 else list1
        return head.next

