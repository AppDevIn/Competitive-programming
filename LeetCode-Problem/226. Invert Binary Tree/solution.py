# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def df(curr):
            if not curr:
                return 
            tmpLeft = curr.left
            curr.left = curr.right
            curr.right = tmpLeft

            df(curr.left)
            df(curr.right)
        df(root)
        return root
        
