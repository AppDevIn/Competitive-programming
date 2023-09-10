# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
            
        queue = [root]
        res = []
        level, fLevel = 1, 0
        levelL = []
        while queue:
            node = queue.pop(0)
            levelL.append(node.val)
            if node.left: 
                fLevel += 1
                queue.append(node.left)
            if node.right: 
                fLevel += 1
                queue.append(node.right)
            
            level -= 1
            if level == 0:
                res.append(levelL)
                levelL = []
                level = fLevel
                fLevel = 0
        return res
