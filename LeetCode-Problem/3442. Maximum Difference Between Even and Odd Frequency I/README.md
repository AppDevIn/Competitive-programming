# [3442. Maximum Difference Between Even and Odd Frequency I](https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/description/?envType=daily-question&envId=2025-06-10)

You are given a string <code>s</code> consisting of lowercase English letters.

Your task is to find the **maximum**  difference <code>diff = freq(a<sub>1)</sub> - freq(a<sub>2</sub>)</code> between the frequency of characters <code>a<sub>1</sub></code> and <code>a<sub>2</sub></code> in the string such that:

- <code>a<sub>1</sub></code> has an **odd frequency**  in the string.
- <code>a<sub>2</sub></code> has an **even frequency**  in the string.

Return this **maximum**  difference.

**Example 1:** 

<div class="example-block">
Input: s = "aaaaabbc"

Output: 3

Explanation:

- The character <code>'a'</code> has an **odd frequency**  of <code>5</code>, and <code>'b'</code> has an **even frequency**  of <code>2</code>.
- The maximum difference is <code>5 - 2 = 3</code>.

**Example 2:** 

<div class="example-block">
Input: s = "abcabcab"

Output: 1

Explanation:

- The character <code>'a'</code> has an **odd frequency**  of <code>3</code>, and <code>'c'</code> has an **even frequency**  of 2.
- The maximum difference is <code>3 - 2 = 1</code>.

**Constraints:** 

- <code>3 <= s.length <= 100</code>
- <code>s</code> consists only of lowercase English letters.
- <code>s</code> contains at least one character with an odd frequency and one with an even frequency.
