Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        self._preOrderTraversal(root, lst)
        return lst
        
    
    def _preOrderTraversal(self, root:Optional[TreeNode], lst:List[int]) -> List[int]:
        if not root: return None
        
        lst.append(root.val)
        self._preOrderTraversal(root.left, lst)
        self._preOrderTraversal(root.right, lst)
        return None
        
        
