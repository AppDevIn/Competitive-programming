### [560\. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

Difficulty: **Medium**  

Related Topics: [Array](https://leetcode.com/tag/array/), [Hash Table](https://leetcode.com/tag/hash-table/), [Prefix Sum](https://leetcode.com/tag/prefix-sum/)


Given an array of integers `nums` and an integer `k`, return _the total number of continuous subarrays whose sum equals to `k`_.

**Example 1:**

```
Input: nums = [1,1,1], k = 2
Output: 2
```

**Example 2:**

```
Input: nums = [1,2,3], k = 3
Output: 2
```

**Constraints:**

*   `1 <= nums.length <= 2 * 10<sup>4</sup>`
*   `-1000 <= nums[i] <= 1000`
*   `-10<sup>7</sup> <= k <= 10<sup>7</sup>`


#### Solution

Language: **Python**

```python
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
​
        hashSet = {0: 1}
        result = 0
        l = []
        for n in nums:
            l.append(n)
            t = sum(l)
            s = t - k
            result += hashSet.get(s, 0)
            hashSet[t] = hashSet.get(t, 0) + 1
            
        return result
​
```