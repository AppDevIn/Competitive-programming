class Solution:
    def findMax(self,root):
        if root is None:
            return float('-inf')
        stack = [root]
        maximum = root.data
        while (stack):
            node = stack.pop(0)
            maximum = max(maximum, node.data)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return maximum
        
    def findMin(self,root):
        if root is None:
            return float('inf')
        stack = [root]
        minimum = root.data
        while (stack):
            node = stack.pop(0)
            minimum = min(minimum, node.data)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return minimum

