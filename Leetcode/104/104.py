# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.rcur(root, 0) if root is not None else 0

    def rcur(self, node: TreeNode, depth: int) -> int:
        right_depth, left_depth = 0, 0
        if node.left:
            left_depth = self.rcur(node.left, depth+1)
        if node.right:
            right_depth = self.rcur(node.right, depth+1)

        if right_depth > left_depth:
            return right_depth
        else:
            return left_depth



