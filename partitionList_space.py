"""
Given a list and a number x, shift all numbers less than x to the left of the list
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

def printNode(head):

    while head:
        print head.val
        head = head.next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        if not head:
            return None

        lesser = []
        greater = []

        while head:
            if head.val < x:
                lesser += [head.val]
            else:
                greater += [head.val]
            head = head.next
        lesser = lesser + greater
        
        current = ListNode(lesser[0])
        head = current

        for val in lesser[1:]:
            current.next = ListNode(val)
            current = current.next

        return head


head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)
x = 3

#printNode(head)

printNode(Solution().partition(head, x))