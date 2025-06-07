# [3170. Lexicographically Minimum String After Removing Stars](https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/description/?envType=daily-question&envId=2025-06-07)

You are given a string <code>s</code>. It may contain any number of <code>'*'</code> characters. Your task is to remove all <code>'*'</code> characters.

While there is a <code>'*'</code>, do the following operation:

- Delete the leftmost <code>'*'</code> and the **smallest**  non-<code>'*'</code> character to its left. If there are several smallest characters, you can delete any of them.

Return the <button type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="radix-:rs:" data-state="closed" class="">lexicographically smallest</button> resulting string after removing all <code>'*'</code> characters.

**Example 1:** 

<div class="example-block">
Input: s = "aaba*"

Output: "aab"

Explanation:

We should delete one of the <code>'a'</code> characters with <code>'*'</code>. If we choose <code>s[3]</code>, <code>s</code> becomes the lexicographically smallest.

**Example 2:** 

<div class="example-block">
Input: s = "abc"

Output: "abc"

Explanation:

There is no <code>'*'</code> in the string.

**Constraints:** 

- <code>1 <= s.length <= 10^5</code>
- <code>s</code> consists only of lowercase English letters and <code>'*'</code>.
- The input is generated such that it is possible to delete all <code>'*'</code> characters.
