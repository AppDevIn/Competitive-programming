class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index = len(numbers)-1
        for i,x in enumerate(numbers):
            find = target - x
            while index >= 0 and numbers[index] >= find:
                if numbers[index] == find: return [i+1, index+1]
                index -= 1
        return []
