### [24\. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)

Difficulty: **Medium**  

Related Topics: [Linked List](https://leetcode.com/tag/linked-list/), [Recursion](https://leetcode.com/tag/recursion/)


Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg)

```
Input: head = [1,2,3,4]
Output: [2,1,4,3]
```

**Example 2:**

```
Input: head = []
Output: []
```

**Example 3:**

```
Input: head = [1]
Output: [1]
```

**Constraints:**

*   The number of nodes in the list is in the range `[0, 100]`.
*   `0 <= Node.val <= 100`


#### Solution

Language: **Python3**

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
​
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
​
        if not head or not head.next:
            return head
​
        first, second = head, head.next
        if not head.next.next:
            second.next = first
            first.next = None
            head = second
        else:
            first.next = second.next
            second.next = first
            head = second
            first.next = self.swapPairs(head.next.next)
​
        return head
```