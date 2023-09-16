# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        hashMap = {value: index for index, value in enumerate(inorder)}
        
        def df(l, r):
            if l > r:
                return None

            root = TreeNode(postorder.pop(-1))
            index = hashMap[root.val]
            root.right = df(index+1, r)
            root.left = df(l, index-1)
            return root
        return df(0, len(inorder)-1)
        
        
            
        
        
        
