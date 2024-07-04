# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        ptr, fast = curr, curr.next

        value = 0
        while fast:
            value += ptr.val 
            if fast.val == 0:
                ptr.val = value
                curr.next = ptr
                curr = curr.next
                value = 0
            
            
            ptr, fast = fast, fast.next
        curr.next = None
        return head.next
