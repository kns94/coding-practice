# Definition for an interval.
class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        
        sorted_start = sorted((interval.start, index) for index, interval in enumerate(intervals))
        sorted_end = sorted((interval.end, index) for index, interval in enumerate(intervals))
        length = len(intervals)
        result = [-1] * length

        print sorted_start
        print sorted_end

        i = 0
        for start in sorted_start:
            print start, i
            while start[0] >= sorted_end[i][0]:
                print i
                print result
                result[sorted_end[i][1]] = start[1]
                i += 1
        return result

intervals = []
intervals += [Interval(1, 12), Interval(2, 9), Interval(3, 10), Interval(13, 14), Interval(15, 16), Interval(16, 17)]

print Solution().findRightInterval(intervals)