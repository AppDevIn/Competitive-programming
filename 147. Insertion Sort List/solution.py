# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.endOfLoop = True
        def helper(prevVal,node):
            
            if not node:
                self.endOfLoop = False
                return None
            
            if prevVal and node.val < prevVal:
                tmp = node.val
                node.val = prevVal
                return tmp
            
            output = helper(node.val, node.next)
            if output is not None:
                node.val = output
            
            if prevVal is not None and node.val < prevVal:
                tmp = node.val
                node.val = prevVal
                return tmp
            else: return None
        
        while self.endOfLoop:
            helper(None, head)
        return head
            
        
            
                
                
            
           
            
            
            
            
