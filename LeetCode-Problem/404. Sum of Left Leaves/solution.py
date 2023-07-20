# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        
        return self._sumOfLeftLeaves(root, False)

    def _sumOfLeftLeaves(self, root: Optional[TreeNode], Left):
        left, right = 0, 0

        if not root.left and not root.right and Left:
            return root.val
        elif not root.left and not root.right and not Left:
            return 0
        if root.left:
            left = self._sumOfLeftLeaves(root.left, True) 
        if root.right:    
            right = self._sumOfLeftLeaves(root.right, False) 
        
        return left + right

