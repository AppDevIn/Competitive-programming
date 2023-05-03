"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        self._flatten(curr)
        return head
    
    def _flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        while curr:
            if curr.child:
                if curr.next:
                    tmp = curr.next
                    returned = self._flatten(curr.child)
                    curr.next = curr.child
                    curr.child.prev = curr
                    curr.child = None
                    returned.next = tmp
                    tmp.prev = returned
                    curr = curr.next
                else:
                    curr.next = curr.child
                    curr.child.prev = curr
                    curr.child = None
            elif not curr.next:
                return curr

            curr = curr.next

        return head
    
    
