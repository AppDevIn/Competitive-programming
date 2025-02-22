#Your task is to complete this function

class BST:
    
    #Function to search a node in BST.
    def search(self, node, x):
        if node is None: 
            return 0 
        if x == node.data:
            return node.data
        elif x > node.data:
            return self.search(node.right, x)
        elif x < node.data:
            return self.search(node.left, x)

