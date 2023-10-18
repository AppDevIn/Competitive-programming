"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        count = 0
        if not root: return 0

        def df(node, count):
            m = count

            if not node.children:
                return m

            for ns in node.children:
                m = max(df(ns, count + 1), m)
            return m
        
        return df(root, 1) 
