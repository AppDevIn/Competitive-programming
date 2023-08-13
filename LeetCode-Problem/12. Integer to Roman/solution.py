class Solution:
    def intToRoman(self, num: int) -> str:

        decimal_values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        roman_numerals = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        count = -1
        ans = ""
        while num > 0:
            if num >= decimal_values[count]:
                ans = ans + roman_numerals[count]
                num -= decimal_values[count]
            else:
                count -= 1
        return ans
