# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        arr = []
        def height(node, h):
            if not node:
                return h
            
            left = height(node.left, h+1)
            right = height(node.right, h+1)
            arr.append(abs(left-right) <= 1)
            if left > right:
                return left
            else: return right

        height(root, 0)
        return False not in arr 
        
