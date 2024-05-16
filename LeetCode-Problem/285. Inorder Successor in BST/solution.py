# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        self.Next = False

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            if self.Next:
                self.ans = root
                self.Next = False
            if p.val == root.val:
                self.Next = True
            inorder(root.right)

        self.ans = None
        inorder(root)
        return self.ans

