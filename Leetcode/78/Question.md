### [78\. Subsets](https://leetcode.com/problems/subsets/)

Difficulty: **Medium**  

Related Topics: [Array](https://leetcode.com/tag/array/), [Backtracking](https://leetcode.com/tag/backtracking/), [Bit Manipulation](https://leetcode.com/tag/bit-manipulation/)


Given an integer array `nums` of **unique** elements, return _all possible subsets (the power set)_.

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

**Example 1:**

```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

**Example 2:**

```
Input: nums = [0]
Output: [[],[0]]
```

**Constraints:**

*   `1 <= nums.length <= 10`
*   `-10 <= nums[i] <= 10`
*   All the numbers of `nums` are **unique**.


#### Solution

Language: **Python3**

```python3
import copy
​
​
class Solution:
    def subsets(self, nums):
        lst = []
​
        for i, x in enumerate(nums):
            arr = []
            arr.append([x])
            if i is not 0:
​
                for j in lst:
                    j = copy.deepcopy(j)
                    j.append(x)
                    arr.append(j)
​
            lst+=arr
        lst.insert(0, [])
        return lst
​
```