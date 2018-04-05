"""Check if permutation of a string is in another string or not"""

class Solution(object):

    def wordCount(self, word):
        wc = {}
        for w in word:
            wc.setdefault(w, 0)
            wc[w] += 1
        return wc

    def dictSubtract(self, wc1, wc2):
        wc = {key: wc1[key] - wc2.get(key, 0) for key in wc1.keys()}
        print wc1, wc2
        print wc
        wc = {key: wc[key] for key in wc.keys() if wc[key] <= 0}
        return wc

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        if len(s1) == 0 or len(s2) == 0 or len(s1) > len(s2):
            return False

        i = 0
        wc = self.wordCount(s1)
        constructed = ''

        while i < len(s2):
            #print i, s2[i], constructed, wc

            if s2[i] in wc:
                constructed += s2[i]
                match = True
                wc[s2[i]] -= 1

                if wc[s2[i]] == 0:
                    del wc[s2[i]]
            else:
                if len(constructed) != 0:
                    constructed += s2[i]
                    constructed = constructed[1:]
                    wc = self.dictSubtract(self.wordCount(s1), self.wordCount(constructed))
            i += 1
            if len(wc.keys()) == 0:
                return True
        return False

s1 = "trinitrophenylmethylnitramine"
s2 = "dinitrophenylhydrazinetrinitrophenylmethylnitramine"
print Solution().checkInclusion(s1, s2)