# Definition for an interval.
class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class TreeNode(object):
    def __init__(self, val, index, left = None, right = None):
        self.val = val
        self.index = index
        self.left = left
        self.right = right

def insertNode(root, node):
    """
    Insert a node 
    """

    if root is None: 
        return node

    if node.val <= root.val:
        root.left = insertNode(root.left, node)
    elif node.val > root.val:
        root.right = insertNode(root.right, node)

    return root

def searchGreaterNode(root, val_to_search):
    """
    Get index of next biggest
    """

    if val_to_search == root.val:
        return root.index

    if not root.left and not root.right:
        if root.val < val_to_search:
            return -1
        else:
            return root.index

    if val_to_search < root.val:
        if not root.left or root.left.val < val_to_search:
            return root.index 
        else:
            return searchGreaterNode(root.left, val_to_search)

    if val_to_search > root.val:
        if not root.right:# or val_to_search > root.right.val:
            return -1
        else:
            return searchGreaterNode(root.right, val_to_search)


class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        
        root = None

        for i in range(len(intervals)):
            start_val = intervals[i].start
            
            if not root:
                root = TreeNode(start_val, i)
            else:
                insertNode(root, TreeNode(start_val, i))
         
        for i in range(len(intervals)):
            end_val = intervals[i].end 
            index = searchGreaterNode(root, end_val)
            intervals[i] = index
                
        return intervals

def printTree(root):

    print root.val

    if root.left:
        printTree(root.left) 
    if root.right:
        printTree(root.right)

intervals = []
intervals += [Interval(3, 4), Interval(2, 3), Interval(1, 2)]

intervals = []
intervals += [Interval(1, 4), Interval(2, 3), Interval(3, 4)]

intervals = []
intervals += [Interval(1, 2)]

intervals = []
intervals += [Interval(1, 12), Interval(2, 9), Interval(3, 10), Interval(13, 14), Interval(15, 16), Interval(16, 17)]

print Solution().findRightInterval(intervals)

#root = TreeNode(1, 0)
#insertNode(root, TreeNode(0, -1))
#insertNode(root, TreeNode(3, -1))
#insertNode(root, TreeNode(5, -1))
#insertNode(root, TreeNode(-1, -1))
#printTree(root)