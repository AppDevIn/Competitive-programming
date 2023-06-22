class Solution:
    def isHappy(self, n: int) -> bool:

        s = set()

        while n != 1:

            n = sum([int(x) ** 2 for x in str(n)])

            if n in s:
                return False
            else:
                s.add(n)

        return True

        
