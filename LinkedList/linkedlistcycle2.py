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

# What they are looking for
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        try:
            curr = head
            fast = head.next
            while(curr is not fast):
                curr = curr.next
                fast = fast.next.next
        except:
            return None
        
        curr = curr.next
        while(head is not curr):
            head = head.next
            curr = curr.next
            
        return head
            
            