class Solution:
    def countAndSay(self, n: int) -> str:
        

        prev = "1"
        
        for i in range(n-1):
            new = ""
            count = 0
            while count <= len(prev) - 1:
                c = 1
                while count+1 <= len(prev)- 1 and prev[count] == prev[count+1]:
                    count += 1
                    c += 1
                new += f"{c}{prev[count]}" 
                
                count += 1
            prev = new

        return prev

        
