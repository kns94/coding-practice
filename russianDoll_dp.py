"""The russian doll algorithm"""

import operator

class Solution(object):

    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """

        """If no nodes are present"""
        if len(envelopes) == 0:
            return 0

        sorted_envelopes = []
        envelopes = sorted(envelopes, key = operator.itemgetter(1))
        
        for i in range(len(envelopes)):
            sorted_envelopes.append([envelopes[i][0], envelopes[i][1], i])

        lis = []
        sorted_envelopes = sorted(sorted_envelopes, key = operator.itemgetter(0))        
        lis.append(sorted_envelopes[0])
        print(envelopes)
        print(sorted_envelopes)

        for i in range(1, len(sorted_envelopes)):
            if sorted_envelopes[i][2] > lis[-1][2]:

                if sorted_envelopes[i][0] > lis[-1][0]:
                    #Extend
                    if sorted_envelopes[i][1] > lis[-1][1]:
                        lis.append(sorted_envelopes[i])
                else:
                    #Discard
                    if sorted_envelopes[i][0] > lis[-2][0] and sorted_envelopes[i][1] > lis[-2][1]:
                        lis = lis[:-1]
                        lis.append(sorted_envelopes[i])
                    else:
                        if sorted_envelopes[i][1] > lis[-1][1]:
                            lis.append(sorted_envelopes[i])


        print(lis)
        return len(lis)


input = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
#input = [[2,1],[4,1],[6,2],[8,3],[10,5],[12,8],[14,13],[16,21],[18,34],[20,55]]
#input = [[30,50],[12,2],[3,4],[12,15]]
#input = [[15,22],[8,34],[44,40],[9,17],[43,23],[4,7],[20,8],[30,46],[39,36],[45,14],[24,19],[24,36],[31,34],[32,19],[29,13],[16,48],[8,36],[44,2],[11,5],[2,50],[29,6],[18,38],[15,49],[22,37],[6,20],[25,11],[1,50],[19,40],[45,35],[37,21],[4,29],[40,5],[4,49],[1,45],[14,32],[14,37],[23,22],[31,21],[2,36],[43,4],[21,32],[41,2],[44,32],[36,20],[22,45],[3,41],[44,29],[29,33],[42,2],[38,17],[43,26],[30,15],[28,12],[33,30],[49,7],[8,14],[1,9],[41,25],[7,15],[26,32],[11,33],[12,45],[33,7],[16,34],[39,1],[20,49],[50,45],[14,29],[50,41],[1,45],[14,43],[49,20],[41,37],[43,22],[45,19],[20,21],[28,19],[2,1],[7,49],[3,3],[49,48],[34,35],[10,2]]
print(Solution().maxEnvelopes(input))       