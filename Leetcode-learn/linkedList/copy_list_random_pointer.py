"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        new_head = Node(head.val)
        curr, curr_new = head, new_head
        while curr.next:
            curr_new.next = Node(curr.next.val)
            curr = curr.next
            curr_new = curr_new.next
            
        curr, curr_new = head, new_head
        while curr:
            if not curr.random: 
                curr = curr.next
                curr_new = curr_new.next
                continue 
            first, second = head, new_head
            random = None
            while first and not random:
                if curr.random == first:
                    random = second
                else:
                    first = first.next
                    second = second.next
            if not random:
                random = second
            curr_new.random = random
            curr = curr.next
            curr_new = curr_new.next
                
        
        return new_head
        
        
        
        
