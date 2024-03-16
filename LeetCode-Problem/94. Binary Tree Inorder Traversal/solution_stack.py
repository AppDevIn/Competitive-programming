# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        q = [root]
        ans = []
        checked = []
        while  q:
            node = q[0]
            index = 0
            if node in checked:
                ans.append(q.pop(0).val)
                continue
            elif not node.left and not node.right:
                ans.append(q.pop(0).val)
                continue

            if node.left:
                q.insert(0, node.left)
                index += 1
            if node.right:
                q.insert(index+1, node.right)
            
            checked.append(node)
            


        return ans

