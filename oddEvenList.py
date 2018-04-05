# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        odd = head
        even = odd.next
        even_first = even

        while True:
            odd.next = even.next 

            if not odd.next:
                break

            odd = odd.next

            even.next = odd.next

            if not even.next:
                break

            even = even.next 

        odd.next = even_first
        return (head)

def printList(head):

    while head:
        print(head.val)
        head = head.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    #head.next.next.next.next = ListNode(5)

    head = Solution().oddEvenList(head)
    printList(head)