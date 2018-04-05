# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        
        n = 0
        head = root

        while head:
            n += 1
            head = head.next

        res = []
        if n >= k:
            rem = (n % k)
            if rem == 0:
                cnt = -1
                small_arr_size = int(n/k)
            else:
                cnt = rem
                small_arr_size = int(n/k) + 1

            while root:
                small_arr = []
                for i in range(small_arr_size):
                    small_arr += [root.val]
                    root = root.next
   
                cnt -= 1             
                if cnt == 0:
                    small_arr_size -= 1

                res += [small_arr]
        else:
            while root:
                res += [[root.val]]
                root = root.next

            for i in range(k - n):
                res += [[]]

        return res

root = ListNode(0)
root.next = ListNode(1)
root.next.next = ListNode(2)
root.next.next.next = ListNode(3)
root.next.next.next.next = ListNode(4)
print Solution().splitListToParts(root, 6)