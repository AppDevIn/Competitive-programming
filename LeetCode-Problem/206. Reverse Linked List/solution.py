# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        self.ans = ListNode(val=head.val)
        
        def helper(node):
            if not node: return 
            tmp = node.next
            node.next = None
            node.next = self.ans
            self.ans = node
            helper(tmp)
        
        helper(head.next)
        return self.ans



        
        
