# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[int]:
        hashSet = self.rcur(root, 0) if root is not None else []
        if not hashSet:
            return []
        value = []
        for i in range(len(hashSet.keys())):
            value.append(hashSet.get(i))
        return value

    def rcur(self, node: TreeNode, depth) -> {}:
        left_lst, right_lst = {}, {}
        if node.left:
            left_lst = self.rcur(node.left, depth + 1)
        if node.right:
            right_lst = self.rcur(node.right, depth + 1)

        hashSet = {}

        for k, v in left_lst.items():
            arr = hashSet.get(k, [])
            arr += v
            hashSet[k] = arr

        for k, v in right_lst.items():
            arr = hashSet.get(k, [])
            arr += v
            hashSet[k] = arr

        arr = []
        if node.val is not None:
            arr = hashSet.get(depth, [])
            arr.append(node.val)
        hashSet[depth] = arr

        return hashSet

