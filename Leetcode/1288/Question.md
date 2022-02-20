### [1288\. Remove Covered Intervals](https://leetcode.com/problems/remove-covered-intervals/)

Difficulty: **Medium**  

Related Topics: [Array](https://leetcode.com/tag/array/), [Sorting](https://leetcode.com/tag/sorting/)


Given an array `intervals` where `intervals[i] = [l<sub style="display: inline;">i</sub>, r<sub style="display: inline;">i</sub>]` represent the interval `[l<sub style="display: inline;">i</sub>, r<sub style="display: inline;">i</sub>)`, remove all intervals that are covered by another interval in the list.

The interval `[a, b)` is covered by the interval `[c, d)` if and only if `c <= a` and `b <= d`.

Return _the number of remaining intervals_.

**Example 1:**

```
Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
```

**Example 2:**

```
Input: intervals = [[1,4],[2,3]]
Output: 1
```

**Constraints:**

*   `1 <= intervals.length <= 1000`
*   `intervals[i].length == 2`
*   `0 <= l<sub style="display: inline;">i</sub> <= r<sub style="display: inline;">i</sub> <= 10<sup>5</sup>`
*   All the given intervals are **unique**.


#### Solution

Language: **Python**

```python
class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
​
        intervals.sort(key=lambda x: (x[0], -x[1]))
        n = len(intervals)
        max = 0
​
        for interval in intervals:
            if interval[1] > max:
                max = interval[1]
            else:
                n -= 1
​
        return n
​
```