# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        prev, curr = head, head.next

        lst = []
        minValue = float("inf")
        index = 1

        while curr.next:
            GREATERTHAN = prev.val < curr.val > curr.next.val
            LESSERTHAN = prev.val > curr.val < curr.next.val
            if GREATERTHAN or LESSERTHAN:
                if len(lst) > 0:
                    minValue = min(minValue, abs(lst[-1] - index))

                lst.append(index)

            index += 1
            prev = curr
            curr = curr.next

        return [minValue, abs(lst[0] - lst[-1])] if len(lst) > 1 else [-1, -1]

