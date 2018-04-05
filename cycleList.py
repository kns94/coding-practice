"""
Given a LinkedList, find if it contains a cycle or not
"""


# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head is None or head.next is None or head.next.next is None:
            return False

        slow = head.next
        fast = head.next.next

        while slow is not None and fast.next is not None:

            if slow.next is None or fast.next.next is None:
                '''Not a cycle'''
                return False

            if fast == slow:
                '''If both pointers match, its a cycle'''
                return True

            slow = slow.next
            fast = fast.next.next

        return False


if __name__ == "__main__":
    head = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)
    five = ListNode(5)

    head.next = two
    two.next = three
    three.next = four
    four.next = two

    print Solution().hasCycle(head)

    #[-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]