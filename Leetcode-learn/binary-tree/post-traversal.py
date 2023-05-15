Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        self.rcur(root, lst)
        return lst
        
        
    def rcur(self, root: Optional[TreeNode], lst) -> List[int]:
        if not root: return 
        self.rcur(root.left, lst)
        self.rcur(root.right, lst)
        lst.append(root.val)
