### [567\. Permutation in String](https://leetcode.com/problems/permutation-in-string/)

Difficulty: **Medium**  

Related Topics: [Hash Table](https://leetcode.com/tag/hash-table/), [Two Pointers](https://leetcode.com/tag/two-pointers/), [String](https://leetcode.com/tag/string/), [Sliding Window](https://leetcode.com/tag/sliding-window/)


Given two strings `s1` and `s2`, return `true` _if_ `s2` _contains a permutation of_ `s1`_, or_ `false` _otherwise_.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

**Example 1:**

```
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
```

**Example 2:**

```
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
```

**Constraints:**

*   `1 <= s1.length, s2.length <= 10<sup>4</sup>`
*   `s1` and `s2` consist of lowercase English letters.


#### Solution

Language: **Python**

```python
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
​
        s1Arr = self.toOrd(s1)
​
        win_size = len(s1)
        hashSet = {}
​
        for i in range(len(s2)):
            new_arr = s2[i: win_size+i]
            if len(new_arr) < len(s1):
                return False
            s2Arr = self.toOrd(new_arr)
            if s2Arr == s1Arr:
                return True
            else:
                continue
        return False
​
​
    def toOrd(self, arr):
        s = [0] * 26
        for i in arr:
            s[ord(i) - ord('a')] += 1
        return s
```