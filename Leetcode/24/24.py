# 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printNodes(head: ListNode):
    str = ""
    while head:
        if not head.next:
            str += f"{head.val}"
        else:
            str += f"{head.val} => "
        head = head.next

    print(str)


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        first, second = head, head.next
        if not head.next.next:
            second.next = first
            first.next = None
            head = second
            print("Last one")
            print(f"Swapping {head.val} to {head.next.val}")
        else:
            first.next = second.next
            second.next = first
            head = second
            printNodes(head)
            print(f"Swapping {head.val} to {head.next.val}")
            first.next = self.swapPairs(head.next.next)

        return head


s = Solution()
node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
printNodes(s.swapPairs(node))
