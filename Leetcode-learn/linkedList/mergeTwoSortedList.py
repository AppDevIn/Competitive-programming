class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 and not list2:
            return list1
        elif not list1:
            return list2
        elif not list2:
            return list1
        

        answer = ListNode()
        curr = answer
        while list1 and list2:
            curr = curr.next if curr.next else curr
            if list1.val > list2.val:
                curr.val = list2.val
                list2 = list2.next 
            else:
                curr.val = list1.val
                list1 = list1.next 
            curr.next = ListNode()
            
        curr.next = list2 if list2 else list1
        return answer
            

