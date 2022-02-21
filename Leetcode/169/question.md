### [169\. Majority Element](https://leetcode.com/problems/majority-element/)

Difficulty: **Easy**  

Related Topics: [Array](https://leetcode.com/tag/array/), [Hash Table](https://leetcode.com/tag/hash-table/), [Divide and Conquer](https://leetcode.com/tag/divide-and-conquer/), [Sorting](https://leetcode.com/tag/sorting/), [Counting](https://leetcode.com/tag/counting/)


Given an array `nums` of size `n`, return _the majority element_.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

**Example 1:**

```
Input: nums = [3,2,3]
Output: 3
```

**Example 2:**

```
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

**Constraints:**

*   `n == nums.length`
*   `1 <= n <= 5 * 10<sup>4</sup>`
*   `-2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1`

**Follow-up:** Could you solve the problem in linear time and in `O(1)` space?

#### Solution

Language: **Python**

```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
​
        setted = set(nums)
        for x in setted:
            if nums.count(x) > len(nums) / 2:
                return x
​
```