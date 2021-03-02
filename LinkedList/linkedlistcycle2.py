# 142. Linked List Cycle II
# https://leetcode.com/problems/linked-list-cycle-ii/
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        if head == None: return head
        
        arr = []
        curr = head
        while(curr not in arr):
            arr.append(curr)
            if curr.next == None: return None
            curr = curr.next
            
        return curr
            