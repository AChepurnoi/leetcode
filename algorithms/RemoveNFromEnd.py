# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodes = {}
        count = 0
        node = head
        while node:
            nodes[count] = node
            node = node.next
            count += 1
        
        delete_index = count - n
        if delete_index == 0:
            return head.next
        else:
            node = nodes[delete_index - 1]
            node.next = node.next.next
            return head

