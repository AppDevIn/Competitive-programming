# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.last =  -2**31 - 1
        def helper(node, left, rootVal):
            if not node: return True
            
            first = helper(node.left, True, node.val)
            ans = node.val > self.last
            self.last = node.val
            second = helper(node.right, False, node.val)
            
            ans = ans and first and second
            
            return ans 

        
            
        left = helper(root.left, True, root.val) 
        ans = root.val > self.last
        self.last = root.val
        right = helper(root.right, False, root.val)

        return ans and left and right
