"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def __init__(self):
        self.leftMost = None
        right = None
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        def printNode(node):
            while node:
                print(node.val)
                node = node.right
            print("Stooped")

        def helper(root):

            if not root.left and not root.right:
                if not self.leftMost:
                    self.leftMost = root

                return root
            
            if root.left:
                left = helper(root.left)
                while left.right:
                    left = left.right
                root.left = left
                left.right = root
            
            if root.right:
                right = helper(root.right)
                while right.left:
                    right = right.left
                root.right = right
                right.left = root
            
            return root
        ans = helper(root)
        leftMost = ans
        rightMost = ans
        while leftMost.left:
            leftMost = leftMost.left
        while rightMost.right:
            rightMost = rightMost.right
        leftMost.left = rightMost
        rightMost.right = leftMost
        return leftMost
        
            




        
        
