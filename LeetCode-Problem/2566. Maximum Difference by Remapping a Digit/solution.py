class Solution:
    def minMaxDifference(self, num: int) -> int:
    
        num_str = str(num)
        
        maxDic = {i: i for i in range(10)}
        minDic = {i: i for i in range(10)}
        
        for char in num_str:
            digit = int(char)
            if digit < 9:
                maxDic[digit] = 9
                break
        
        first_digit = int(num_str[0])
        minDic[first_digit] = 0
       
        
        max_str = ""
        min_str = ""
        
        for char in num_str:
            digit = int(char)
            max_str += str(maxDic[digit])
            min_str += str(minDic[digit])
        
        max_num = int(max_str)
        min_num = int(min_str)
        
        return max_num - min_num


