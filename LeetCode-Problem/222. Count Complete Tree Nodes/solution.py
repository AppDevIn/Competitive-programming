# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def df(root):
            if not root: 
                return 0
            return df(root.left) + df(root.right) + 1

        return df(root)
        
