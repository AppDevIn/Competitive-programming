# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        def df(root, val, left=True, right=True):
                 
            if not root:
                return False
        
            val += root.val      
            
            if not root.left and not root.right:
                return val == targetSum
        
            return df(root.left, val) or df(root.right, val)
         
        return df(root, 0)
            
            
            
        
