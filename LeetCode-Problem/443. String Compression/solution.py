class Solution:
    def compress(self, chars: List[str]) -> list:
        start, end = 0, 0
        
        while start < len(chars):
            length = 0
            while end < len(chars) and chars[start] == chars[end]:
                end += 1
                length += 1
            end -= 1
            sizeLen = len(str(length))
            while start < end - sizeLen:
                chars.pop(start)
                end -= 1
            if length != 1:
                end -= sizeLen - 1
                for c in str(length):
                    chars[end] = c
                    end += 1
            else:
                end += 1
            start = end 
            

            


        

        
