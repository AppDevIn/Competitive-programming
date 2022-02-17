### [39\. Combination Sum](https://leetcode.com/problems/combination-sum/)

Difficulty: **Medium**  

Related Topics: [Array](https://leetcode.com/tag/array/), [Backtracking](https://leetcode.com/tag/backtracking/)


Given an array of **distinct** integers `candidates` and a target integer `target`, return _a list of all **unique combinations** of_ `candidates` _where the chosen numbers sum to_ `target`_._ You may return the combinations in **any order**.

The **same** number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is **guaranteed** that the number of unique combinations that sum up to `target` is less than `150` combinations for the given input.

**Example 1:**

```
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7\. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
```

**Example 2:**

```
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
```

**Example 3:**

```
Input: candidates = [2], target = 1
Output: []
```

**Constraints:**

*   `1 <= candidates.length <= 30`
*   `1 <= candidates[i] <= 200`
*   All elements of `candidates` are **distinct**.
*   `1 <= target <= 500`


#### Solution

Language: **Python3**

```python3
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        l = []
        for x in candidates:
            l += self.df(target, [x], candidates, {})
        arr = []
        for x in l:
            x.sort()
            if x not in arr:
                arr.append(x)
        arr.sort()
        return arr
​
    def df(self, target, curr_list, candidates, hashSet):
        target = target - curr_list[-1]
        l = []
        if target == 0:
            l.append(curr_list)
            return l
        elif target > 0:
            filtered_list = filter(lambda x: x <= target, candidates)
            for x in filtered_list:
                temp = copy.deepcopy(curr_list)
                temp.append(x)
                l += self.df(target, temp, candidates, hashSet)
        else:
            return []
​
        return l
​
```