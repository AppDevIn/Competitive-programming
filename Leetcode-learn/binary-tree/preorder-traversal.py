# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.rcur(root) if root is not None else []

    def rcur(self, node: TreeNode):
        lst = []
        if node.val != None:
            lst.append(node.val)
        if node.left:
            lst += self.rcur(node.left)
        if node.right:
            lst += self.rcur(node.right)

        return lst
