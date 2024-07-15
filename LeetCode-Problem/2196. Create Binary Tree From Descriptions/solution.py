# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children = set()
        parents = set()

        parentsToChildren = {}

        for d in descriptions:
            parent, child, isLeft = d

            parents.add(parent)
            parents.add(child)
            children.add(child)

            if parent not in parentsToChildren:
                parentsToChildren[parent] = []

            parentsToChildren[parent].append((child, isLeft))

        for parent in parents.copy():
            if parent in children:
                parents.remove(parent)

        root = TreeNode(parents.pop())
        queue = deque([root])

        while queue:
            parent = queue.popleft()

            for childValue, isLeft in parentsToChildren.get(parent.val, []):
                child = TreeNode(childValue)
                queue.append(child)

                if isLeft:
                    parent.left = child
                else:
                    parent.right = child
        return root

