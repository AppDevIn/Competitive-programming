class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
        
class MyLinkedList:
    
    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        
        curr = self._traverse(index)
        
        return curr.val if curr else -1
        

    def addAtHead(self, val: int) -> None:
        head = Node(val)
        if self.head == None :
            self.head = head
            return None
        
        head.next = self.head
        self.head = head
        self.size += 1
        
        

    def addAtTail(self, val: int) -> None:
        tail = Node(val)
        if self.head == None:
            self.head = tail
            return None
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = tail
        self.size += 1
            
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            self.size +=1
            return None
        
        curr = self._traverse(index-1)
        
        if not curr: return None
        
        node = Node(val)
        node.next = curr.next
        curr.next = node
        self.size += 1
            
        

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        if index == 0 and self.head.next:
            self.head = self.head.next
            self.size += 1
            return None
        elif index == 0 and not self.head.next:
            self.head = None
            self.size += 1
            return None
    
        curr = self._traverse(index-1)
        if curr and curr.next:
            curr.next = curr.next.next
        
    def _traverse(self, index):
        if index > self.size : return None
        curr = self.head
        curr_index = 0
        while curr_index != index:
            curr = curr.next
            curr_index += 1
        return curr
    


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
