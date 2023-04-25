class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        leftover = True
        index = len(digits) - 1
        while leftover:
            sum = digits[index] + 1

            if sum > 9 and index == 0:
                digits[index] = sum - 10
                digits.insert(0, 1)
                leftover = False
            elif sum > 9:
                digits[index] = sum - 10
                leftover = True
            else:
                digits[index] = sum
                leftover = False
            index -= 1

        return digits
