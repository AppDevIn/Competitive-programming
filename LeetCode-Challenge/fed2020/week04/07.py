# 895. Maximum Frequency Stack
# https://leetcode.com/problems/maximum-frequency-stack/
# Code failed at test case 37 with timit limit exceed
class FreqStack:

    def __init__(self):
        self.arr = []
        self.dict = {}
        self.freq = {}

    def push(self, x: int) -> None:
        self.arr.append(x)
        
        if x in self.dict.keys():
            value = self.dict.get(x) + 1
            self.dict[x] = value

            if value in self.freq.keys():
                if value - 1 in self.freq.keys() and x in self.freq.get(value-1):
                    self.freq.get(value-1).remove(x)
                self.freq[value].append(x)
            else:
                if value - 1 in self.freq.keys() and x in self.freq.get(value-1):
                    self.freq.get(value-1).remove(x)
                self.freq[value] = [x]

        else:
            value = 1
            self.dict[x] = value

            if value in self.freq.keys() :
                if value - 1 in self.freq.keys() and x in self.freq.get(value-1):
                    self.freq.get(value-1).remove(x)
                self.freq[value].append(x)
            else:
                 self.freq[value] = [x]
            
        

    def pop(self) -> int:
        maxV  = max(self.dict.values())
        
        
        for i in range(len(self.arr)-1, -1, -1):
            
            if self.arr[i] in self.freq[maxV]: 

                self.dict[self.arr[i]] = self.dict.get(self.arr[i]) - 1
                x = self.arr.pop(i)

                value = self.dict.get(x)
                

                if value in self.freq.keys():
                    if value + 1 in self.freq.keys() and x in self.freq.get(value+1):
                        self.freq.get(value+1).remove(x)
                    self.freq[value].append(x)
                else:
                    if value + 1 in self.freq.keys() and x in self.freq.get(value+1):
                        self.freq.get(value+1).remove(x)
                    self.freq[value] = [x]
                return x


                
            
            
# Your FreqStack object will be instantiated and called as such:
obj = FreqStack()
obj.push(5)
obj.push(7)
obj.push(5)
obj.push(7)
obj.push(4)
obj.push(5)
print(obj.pop())
print(obj.pop())