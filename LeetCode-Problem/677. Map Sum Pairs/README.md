class TrieNode:
    def __init__(self):
        self.value = 0
        self.nodes = {}
class MapSum:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        for c in key:
            if c not in curr.nodes:
                curr.nodes[c] = TrieNode()
            curr = curr.nodes[c]
        curr.value = val
        
    def calcSum(self, node):
        s = 0
        if node.value > 0:
            s = node.value
            
        
        for n in node.nodes.keys():
            s += self.calcSum(node.nodes[n])
            
        return s
    def sum(self, prefix: str) -> int:
        curr = self.root
        for c in prefix:
            if c not in curr.nodes:
                return 0
            curr = curr.nodes[c]    
        
        
        return self.calcSum(curr)
        
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
