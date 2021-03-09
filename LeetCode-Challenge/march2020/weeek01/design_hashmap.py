# 706. Design HashMap
# https://leetcode.com/problems/design-hashmap/
class Node:
    def __init__(self, val, key, next=None):
        self.key = key
        self.val = val
        self.next = next
        
class MyHashMap:
    arr = []

    def hash(self,key) -> int:
        return key % 100

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [None] * 100

    
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """

        hashValue = self.hash(key)

        if self.arr[hashValue] == None:
            self.arr[hashValue] = Node(value, key=key)
        else:
            curr = self.arr[hashValue]
        
            while True:
                if curr.key == key:
                    curr.val = value
                    return
                if curr.next == None:break
                    
                curr = curr.next
            curr.next = Node(value, key=key)
            
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """

        hashValue = self.hash(key)

        curr = self.arr[hashValue]
        while curr != None:
            if curr.key == key:
                return curr.val
            curr = curr.next 
        return -1

        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hashValue = self.hash(key)
        
        

        if self.arr[hashValue] == None: return 

        curr = prev = self.arr[hashValue]

        if curr.key == key:
            self.arr[hashValue] = self.arr[hashValue].next
        else:
            curr = curr.next
            while curr != None :
                if curr.key == key:
                    prev.next = curr.next
                    break
                else:
                    prev, curr = curr, curr.next



            
            



obj = MyHashMap()
obj.put(1,1)
obj.put(2,2)
param_2 = obj.get(1)
obj.get(3)
obj.put(2,1)
param_2 = obj.get(2)
obj.remove(2)
param_2 = obj.get(2)