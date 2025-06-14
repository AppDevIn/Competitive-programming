# [2566. Maximum Difference by Remapping a Digit](https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/description/?envType=daily-question&envId=2025-06-14)

You are given an integer <code>num</code>. You know that Bob will sneakily **remap**  one of the <code>10</code> possible digits (<code>0</code> to <code>9</code>) to another digit.

Return the difference between the maximum and minimumvalues Bob can make by remapping**exactly**  **one**  digit in <code>num</code>.

**Notes:** 

- When Bob remaps a digit d1to another digit d2, Bob replaces all occurrences of <code>d1</code>in <code>num</code>with <code>d2</code>.
- Bob can remap a digit to itself, in which case <code>num</code>does not change.
- Bob can remap different digits for obtaining minimum and maximum values respectively.
- The resulting number after remapping can contain leading zeroes.

**Example 1:** 

```
Input: num = 11891
Output: 99009
Explanation: 
To achieve the maximum value, Bob can remap the digit 1 to the digit 9 to yield 99899.
To achieve the minimum value, Bob can remap the digit 1 to the digit 0, yielding 890.
The difference between these two numbers is 99009.
```

**Example 2:** 

```
Input: num = 90
Output: 99
Explanation:
The maximum value that can be returned by the function is 99 (if 0 is replaced by 9) and the minimum value that can be returned by the function is 0 (if 9 is replaced by 0).
Thus, we return 99.```

**Constraints:** 

- <code>1 <= num <= 10^8</code>
