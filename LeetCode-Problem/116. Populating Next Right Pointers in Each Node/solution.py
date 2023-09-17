"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        queue = [root]
        
        while queue:
            tmpQ = []
            while queue:
                node = queue.pop(0)
                if queue:
                    node.next = queue[0]
                else:
                    node.next = None 
                    
                if node.left:
                    tmpQ.append(node.left)
                if node.right:
                    tmpQ.append(node.right)  
            print(tmpQ)
            queue = tmpQ
        return root
        
