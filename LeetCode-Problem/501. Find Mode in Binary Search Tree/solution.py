# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hashMap = {}
        def df(root):
            if not root:
                return 
            if root.val in hashMap:
                hashMap[root.val] = hashMap[root.val]+1
            else: hashMap[root.val] = 0
            df(root.left)
            df(root.right)
        df(root)
        max_value = max(hashMap.values())

        # Find all keys associated with the maximum value using a loop
        max_keys = []
        for key, value in hashMap.items():
            if value == max_value:
                max_keys.append(key)
        return max_keys
        
                
            
        
