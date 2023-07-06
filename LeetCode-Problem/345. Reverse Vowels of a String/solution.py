class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = set('aeiouAEIOU')
        split_string = list(s)
        
        left, right = 0, len(s) - 1
        
        
        while left < right:
            if split_string[left] not in vowels:
                left += 1
            
            if split_string[right] not in vowels:
                right -= 1
            
            if split_string[left] in vowels and split_string[right] in vowels:
                tmp = s[left]
                split_string[left] = split_string[right]
                split_string[right] = tmp
                left += 1
                right -= 1
     
        return ''.join(split_string) 
