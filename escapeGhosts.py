class Solution(object):

    def getManhattanDistance(self, pointA, pointB):
        """Given two points in a cartesian space - pointA and poinB,
            get Manhattan distance between two points"""

        x_distance = abs(pointA[0] - pointB[0])
        y_distance = abs(pointA[1] - pointB[1])

        return x_distance + y_distance

    def getNextStep(self, point, target):
        """Given a point and a target, get the next step such that is closer
            to the target"""

        min_distance = self.getManhattanDistance(point, target)
        next_step = point 

        #Go Up
        up_distance = self.getManhattanDistance([point[0], point[1] + 1], target)
        if up_distance < min_distance:
            next_step = [point[0], point[1] + 1]
            min_distance = up_distance

        #Go Down
        down_distance = self.getManhattanDistance([point[0], point[1] - 1], target)
        if down_distance < min_distance:
            next_step = [point[0], point[1] - 1]
            min_distance = down_distance

        #Go left
        left_distance = self.getManhattanDistance([point[0] - 1, point[1]], target)
        if left_distance < min_distance:
            next_step = [point[0] - 1, point[1]]
            min_distance = left_distance

        #Go right
        right_distance = self.getManhattanDistance([point[0] + 1, point[1]], target)
        if right_distance < min_distance:
            next_step = [point[0] + 1, point[1]]
            min_distance = right_distance

        return next_step

    def getNearestGhosts(self, ghosts, target):

        ghost_distances = {}

        for ghost in ghosts:
            distance = self.getManhattanDistance(ghost, target)
            new_distance = ghost_distances.setdefault(distance, [])
            ghost_distances[distance] += [ghost]

        return ghost_distances[min(ghost_distances.keys())]

    def findPaths(self, player, ghosts, target):
        """Find if you can reach destination before the ghost"""

        player_distance = self.getManhattanDistance(player, target)

        for ghost in ghosts:
            ghost_distance = self.getManhattanDistance(ghost, target)
            if ghost_distance < player_distance:
                return False
        return True

    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        
        return self.findPaths([0, 0], ghosts, target)

ghosts = [[546,547],[1728,885],[66,67],[-331,-330],[1637,976],[1501,1112],[1414,1199],[2057,556],[1722,891],[1709,904],[151,152],[1492,1121],[-989,-988],[1473,1140],[-585,-584],[1491,1122],[4219,-1606],[4016,-1403],[2398,215],[420,421],[1126,1127],[2337,276],[711,712],[3895,-1282],[-1527,-1526],[1008,1009],[-1134,-1133],[2857,-244],[3413,-800],[687,688],[1840,773],[-949,-948],[874,875],[4165,-1552],[-450,-449],[384,385],[2731,-118],[441,442],[1980,633],[63,64],[1993,620],[3207,-594],[2259,354],[1931,682],[200,201],[-1265,-1264],[3877,-1264],[-173,-172],[4092,-1479],[1851,762],[1509,1104],[2107,506],[3698,-1085],[-424,-423],[-787,-786],[-712,-711],[3465,-852],[2210,403],[3799,-1186],[3111,-498],[2832,-219],[1476,1137],[-525,-524],[2326,287],[2446,167],[1838,775],[-248,-247],[505,506],[-362,-361],[1567,1046],[4288,-1675],[1081,1082],[1799,814],[143,144],[-1153,-1152],[3205,-592],[92,93],[-1669,-1668],[3675,-1062],[1273,1274],[-1230,-1229],[1555,1058],[1648,965],[2735,-122],[340,341],[-608,-607],[2547,66],[3573,-960],[1107,1108],[-1640,-1639],[-764,-763],[1771,842],[3384,-771],[-53,-52],[3021,-408],[-1114,-1113],[-309,-308],[1653,960],[3639,-1026],[2820,-207]]
target = [1306,-1689]
print Solution().escapeGhosts(ghosts, target)