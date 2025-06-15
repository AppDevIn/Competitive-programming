class Solution:
    def maxDiff(self, num: int) -> int:
        index = 0
        num = str(num)
        while index < len(num)-1 and num[index] == "9":
            index += 1
        
        a = ""

        for c in range(len(num)):
            if num[index] == num[c]:
                a += "9"
            else:
                a += num[c]
        

        index = 0
        while index < len(num)-1 and (num[index] == "1" or num[index] == "0"):
                index += 1
        
        b = ""
        for c in range(len(num)):
            if num[index] == num[c]:
                if index == 0 or (num[0] == "1" and num[index] == "1"):
                    b += "1"
                else:
                    b += "0"
            else:
                b += num[c]
        
        print(index)
        return int(a) - int(b)
        
        
