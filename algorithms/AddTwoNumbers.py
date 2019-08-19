"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        start = ListNode(0)
        node = start 
        plus_one = False
        while l1 is not None and l2 is not None:
            value = l1.val + l2.val + int(plus_one)
            plus_one = value > 9 
            if plus_one:
                value = value - 10
            new_node = ListNode(value)
            node.next = new_node
            node = new_node
            l1 = l1.next
            l2 = l2.next
        
        non_empty = l1 if l1 is not None else l2

        while non_empty is not None:
            value = non_empty.val + int(plus_one)
            plus_one = value > 9 
            if plus_one:
                value = value - 10
            new_node = ListNode(value)
            node.next = new_node
            node = new_node
            non_empty = non_empty.next
        
        if plus_one:
            new_node = ListNode(1)
            node.next = new_node
            node = new_node
            
        return start.next
