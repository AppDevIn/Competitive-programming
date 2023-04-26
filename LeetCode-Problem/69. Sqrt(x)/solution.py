class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        left, right = 1, x//2
        
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        
        return right if x != 1 else 1

