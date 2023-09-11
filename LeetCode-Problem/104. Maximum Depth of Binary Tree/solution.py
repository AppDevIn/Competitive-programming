# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def maximum_depth(curr, depth):
            if not curr:
                return depth
            
            left_value = maximum_depth(curr.left, depth+1)
            right_value = maximum_depth(curr.right, depth+1)
            
            return max(left_value, right_value)
        
        return maximum_depth(root, 0)
        
