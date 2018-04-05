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

        h1 = ListNode(0)
        h2 = ListNode(0)
        smaller = h1
        larger = h2

        while head:
            if head.val < x:
                smaller.next = ListNode(head.val)
                smaller = smaller.next
            else:
                larger.next = ListNode(head.val)
                larger = larger.next
            
            head = head.next

        larger.next = None
        smaller.next = h2.next
        return h1.next

head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)
x = 3

#printNode(head)

printNode(Solution().partition(head, x))