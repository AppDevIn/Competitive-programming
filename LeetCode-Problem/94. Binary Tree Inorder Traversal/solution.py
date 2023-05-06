# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self._inorderTraversal(root, [])
    
    def _inorderTraversal(self, root: Optional[TreeNode], lst: List[int]) -> List[int]:
        if root:
            lst = self._inorderTraversal(root.left, lst)
            lst.append(root.val)
            lst = self._inorderTraversal(root.right, lst)
        return lst



