# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None: return None
        count = 1
        node = head

        if head.next:
            tmp = head.next
            head.next = head.next.next
            tmp.next = None
            tmp.next = head
            head = tmp
            node = head
        

        while node.next and node.next.next:
            if count % 2 == 0:
                tmp = node.next
                node.next = node.next.next
                tmp.next = None
                if node.next.next:
                    tmp.next = node.next.next
                    
                node.next.next = tmp
            count += 1
            node = node.next
        return head
        return None 
            

                

