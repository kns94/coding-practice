from operator import itemgetter

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        if len(points) == 0:
            return 0

        points = sorted(points, key = itemgetter(1))
        arr_s = points[0][1]
        arr = 1

        for i in range(1, len(points)):
            current_s = points[i][0]
            current_e = points[i][1]

            if arr_s >= current_s and arr_s <= current_e:
                pass
            else:
                arr += 1
                arr_s = current_e

        return arr

points = [[10,16], [2,8], [1,6], [7,12]]
#points = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
print Solution().findMinArrowShots(points)