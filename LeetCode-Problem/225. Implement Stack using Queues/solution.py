from queue import Queue
class MyStack:

    def __init__(self):
        self.my_queue = Queue()
        

    def push(self, x: int) -> None:
        newQueue = Queue()
        newQueue.put(x)
        
        while not self.my_queue.empty():
            newQueue.put(self.my_queue.get())
        self.my_queue = newQueue
        

    def pop(self) -> int:
        return self.my_queue.get()
        

    def top(self) -> int:
        return self.my_queue.queue[0]
        

    def empty(self) -> bool:
        return self.my_queue.empty()
        
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
