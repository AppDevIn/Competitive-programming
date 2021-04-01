# 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        arr = []
        curr = head
        while(curr):
            arr.append(curr.val)
            curr = curr.next

        return arr == arr[::-1]


s = Solution()


print(s.isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))))
