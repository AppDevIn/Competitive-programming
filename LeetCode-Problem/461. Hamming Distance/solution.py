class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        value = x ^ y

        bitValue, count = 1, 0

        while bitValue < value: bitValue *= 2

        while bitValue >= 1:
            if bitValue <= value:
                value -= bitValue
                count += 1
            bitValue -= bitValue / 2
        return count
