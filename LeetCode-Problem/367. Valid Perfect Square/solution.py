class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        odd = 1
        count = 0
        ori = num
        while num > 0:
            num -= odd
            count += 1
            odd += 2
        
        return count * count == ori
