# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
         
            def df(root, sameNode=True):
                pq = root == p or root == q
                if not root: return pq
                
                left = df(root.left)
                right = df(root.right)
                if type(left) is not bool: return left
                elif type(right) is not bool: return right
                
                
                if left and right:
                    return root
                elif (pq and left) or (pq and right):
                    return root
                elif left or right:
                    return True
                elif pq: return True
                else: return False
                
            val = df(root)
            return  val if val != False else None
