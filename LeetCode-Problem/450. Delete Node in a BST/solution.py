# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def successor(self, root):
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root: TreeNode) -> TreeNode:
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not (root.left or root.right):
                root = None
            elif root.right:
                root.val = self.successor(root.right)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predecessor(root.left)
                root.left = self.deleteNode(root.left, root.val)
        return root

