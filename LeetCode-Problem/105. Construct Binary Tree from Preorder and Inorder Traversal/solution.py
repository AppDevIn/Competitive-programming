# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        idxInorder = {value: index  for index, value in enumerate(inorder)}
        
        def df(l, r):
            if l > r:
                return None
            root = TreeNode(preorder.pop(0))
            idx = idxInorder[root.val]
            root.left = df(l, idx-1)
            root.right = df(idx+1, r)
            return root
        return df(0, len(inorder)-1)
            
            
        
        
