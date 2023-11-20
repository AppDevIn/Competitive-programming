class MovingAverage:

    def __init__(self, size: int):
        self.max = size
        self.arr = [0]*size
        self.size = 0
        self.head = 0
        

    def next(self, val: int) -> float:
        self.arr[self.head] = val
        self.head = (self.head + 1) % (self.max)
        self.size += 1
        return sum(self.arr)/min(self.size, self.max)
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
