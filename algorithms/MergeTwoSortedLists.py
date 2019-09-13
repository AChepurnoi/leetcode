# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        if l1.val < l2.val:
            node = l1
            l1 = l1.next
        else:
            node = l2
            l2 = l2.next

        head = node
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                node = l1
                l1 = l1.next
            else:
                node.next = l2
                node = l2
                l2 = l2.next
        
        tail = l1 if l1 else l2
        while tail:
            node.next = tail
            node = tail
            tail = tail.next
            
        return head
