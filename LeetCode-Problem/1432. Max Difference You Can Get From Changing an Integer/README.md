# [1432. Max Difference You Can Get From Changing an Integer](https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/description/?envType=daily-question&envId=2025-06-15)

You are given an integer <code>num</code>. You will apply the following steps to <code>num</code> **two**  separate times:

- Pick a digit <code>x (0 <= x <= 9)</code>.
- Pick another digit <code>y (0 <= y <= 9)</code>. Note <code>y</code> can be equal to <code>x</code>.
- Replace all the occurrences of <code>x</code> in the decimal representation of <code>num</code> by <code>y</code>.

Let <code>a</code> and <code>b</code> be the two results from applying the operation to <code>num</code> independently.

Return the max difference between <code>a</code> and <code>b</code>.

Note that neither <code>a</code> nor <code>b</code> may have any leading zeros, and **must not**  be 0.

**Example 1:** 

```
Input: num = 555
Output: 888
Explanation: The first time pick x = 5 and y = 9 and store the new integer in a.
The second time pick x = 5 and y = 1 and store the new integer in b.
We have now a = 999 and b = 111 and max difference = 888
```

**Example 2:** 

```
Input: num = 9
Output: 8
Explanation: The first time pick x = 9 and y = 9 and store the new integer in a.
The second time pick x = 9 and y = 1 and store the new integer in b.
We have now a = 9 and b = 1 and max difference = 8
```

**Constraints:** 

- <code>1 <= num <= 10^8</code>
