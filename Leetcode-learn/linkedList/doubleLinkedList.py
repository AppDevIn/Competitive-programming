class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        if index > self.size - 1:
            return -1
        curr = self.head
        while index > 0:
            index -= 1
            curr = curr.next
        return curr.val
            
        

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            self.size += 1
            return None
        
        tH = Node(val)
        tH.next = self.head
        self.head.prev = tH
        self.head = tH
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            self.size += 1
            return None
        
        tT = Node(val)
        
        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = tT
        tT.prev = curr
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return None
        elif index == self.size:
            self.addAtTail(val)
            return None
        
        if index > self.size : return None
        
        curr = self.head
        
        while index-1 > 0: 
            index -= 1
            curr = curr.next

        node = Node(val)
        node.next = curr.next
        node.prev = curr
        curr.next.prev = node
        curr.next = node
        self.size += 1
            

    def deleteAtIndex(self, index: int) -> None: 
        if index == 0 and self.head:
            self.head = self.head.next
            self.size -= 1
            return None
            
        if index >= self.size : return None

        curr = self.head

        while index-1 > 0: 
            index -= 1
            curr = curr.next
        
        
        curr.next = curr.next.next
        if curr.next:
            curr.next.prev = curr
        self.size -= 1
            
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
