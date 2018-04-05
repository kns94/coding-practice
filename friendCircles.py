class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        
        friends = {}
        for i in range(len(M)):
            friends.setdefault(i, [])
            for j in range(len(M)):
                if M[i][j] == 1:
                    friends[i] += [j]

        for k in friends.keys():
            parsed = {}
            if k in friends:
                v = friends[k]
                for sk in v:
                    if sk not in parsed and sk in friends:
                        if sk != k:
                            friends[k] += friends[sk]
                            del friends[sk]
                        parsed[sk] = True

        return len(friends.keys())

M = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print Solution().findCircleNum(M)