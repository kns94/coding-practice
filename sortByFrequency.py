import operator

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) == 0 or len(s) == 1:
            return s
        
        ctr = {}
        res = ''

        for ch in s:
            ctr.setdefault(ch, 0)
            ctr[ch] += 1

        items = sorted(ctr.items(), key = operator.itemgetter(1), reverse = True)

        for item in items:
            res += item[0] * item[1]

        return res

s = 'tree'
print Solution().frequencySort(s)