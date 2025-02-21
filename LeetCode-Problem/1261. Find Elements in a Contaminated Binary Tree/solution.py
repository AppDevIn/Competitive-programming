# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    def __init__(self, root: TreeNode):
        self.root = root
        self.recover_tree(root, 0)

    def recover_tree(self, node: TreeNode, value: int):
        if not node:
            return
        node.val = value
        if node.left:
            self.recover_tree(node.left, 2 * value + 1)
        if node.right:
            self.recover_tree(node.right, 2 * value + 2)

    def find(self, target: int) -> bool:
        return self.dfs(self.root, target)
    
    def dfs(self, node: TreeNode, target: int) -> bool:
        if not node:
            return False
        if node.val == target:
            return True
        return self.dfs(node.left, target) or self.dfs(node.right, target)

        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
