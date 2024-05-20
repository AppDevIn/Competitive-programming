class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class KthLargest:

    def inorder(self, node):
        if not node: return 
        self.inorder(node.left)
        print(node.val)
        self.inorder(node.right)

    def search3Highest(self, node, k):
        self.stack = []
        current = node
        previous = None
        while (current is not None or self.stack) and k > 0:
            
            while current is not None:
                self.stack.append(current)
                current = current.right
            
            k -= 1
            current = self.stack.pop()
            
            previous = current
            current = current.left
        return previous


        

    def insert(self, node, num):
        if not node:
            return TreeNode(num)
        
        if num > node.val:
            node.right = self.insert(node.right, num)
        else:
            node.left = self.insert(node.left, num)
        
        return node
        
            
        


    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.node = None
        for n in nums:
            self.node = self.insert(self.node, n)
        self.kth = self.search3Highest(self.node, k)

        

        

        
        

    def add(self, val: int) -> int:
        self.node = self.insert(self.node, val)
        
        if not self.kth or not self.node.right:
            self.kth = self.search3Highest(self.node, self.k)
        elif self.kth and val > self.kth.val:
            self.kth = self.search3Highest(self.node, self.k)
        return self.kth.val
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
