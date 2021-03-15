# 1721. Swapping Nodes in a Linked List
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        
        
        arr = []
        temp = head
        while(temp != None):
            arr.append(temp)
            temp = temp.next

        t = arr[k-1]
        arr[k-1] = arr[(len(arr) - k)]
        arr[(len(arr) - k)] = t

        
        head = arr[0]
        temp = head
        for x in arr[1:]:
            x.next = None
            temp.next = x
            temp = temp.next
        
        return head

    def swapNodes(self, head: ListNode, k: int) -> ListNode:

        

        first = head
        for _ in range(1, k):
            first = first.next
        fast= first

        slow = head
        while fast.next:
            slow, fast = slow.next, fast.next
        
        slow.val, first.val = first.val, slow.val

        return head



def generateNode(arr=[1,2]) -> ListNode:

    head = ListNode(arr[0])
    temp = head
    for x in arr[1::]:
        temp.next = ListNode(x)
        temp = temp.next
    
    return head

def printNode(root: ListNode):
    temp = root
    while(temp!=None):
        print(temp.val)
        temp = temp.next

s = Solution()
printNode(s.swapNodes(generateNode(), 1))
            