# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def helper(root, value):

            if not root:
                return value
            
            root.val = helper(root.right, value) + root.val
            value = root.val
            return helper(root.left, value)
            
        
        helper(root, 0)

        return root
        
