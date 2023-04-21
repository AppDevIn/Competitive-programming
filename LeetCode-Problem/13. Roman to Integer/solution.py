class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        combo = {'I': ["V","X"], "X": ["L", "C"], "C": ["D", "M"]}
        total_sum = 0
        index = 0
        while index <= len(s)-1:
            
            if index + 1 <= len(s) - 1 and s[index] in combo and s[index+1] in combo[s[index]]:
                total_sum += roman_to_num[s[index+1]] - roman_to_num[s[index]]
                index += 1
            else:
                total_sum += roman_to_num[s[index]]
            index += 1
            print(str(index)+" "+str(total_sum))

        return total_sum
