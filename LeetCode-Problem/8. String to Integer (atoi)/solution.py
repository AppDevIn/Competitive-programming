class Solution:
    def myAtoi(self, s: str) -> int:

        postive = True
        value = ""
        start = False
        index = 0
        for c in s:
            print(value)
            if c == " " and not start: continue
            elif c in "-+" and index == 0: 
                start = True
                postive = c != "-" or c == "+"
            elif c not in "0123456789" and not start: return 0
            elif c not in "0123456789" and start: break
            elif c in "0123456789":
                start = True
                value += c
            
            index += 1
        
        value = value if value != "" else 0  
        value = int(value) if postive else -int(value)

        if -2**31 < value < 2**31-1:
            return value 
        else: 
            return 2**31-1 if postive else -2**31

            

            
