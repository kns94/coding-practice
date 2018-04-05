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

        while True:
            prev = None
            current = head
            swap_count = 0

            while current.next:
                if current.val > current.next.val and current.next.val < x and current.val >= x:
                    swap_count += 1
                    temp = current.next

                    if prev:
                        temp = current.next
                        prev.next = temp
                        current.next = temp.next
                        prev.next.next = current
                        prev = prev.next
                    else:
                        head = current.next
                        current.next = head.next
                        head.next = current
                        prev = head

                else:
                    prev = current
                    current = current.next

            if swap_count == 0:
                break

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