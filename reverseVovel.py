class Solution(object):

    def isVovel(self, ch):

        if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
            return True
        else:
            return False

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s = list(s)
        l, r = 0, len(s) - 1

        while l <= r:

            if self.isVovel(s[l]) and self.isVovel(s[r]):
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif not self.isVovel(s[l]):
                l += 1
            elif not self.isVovel(s[r]):
                r -= 1

        return ''.join(s)


print Solution().reverseVowels('hello')
print Solution().reverseVowels('leetcod')
print Solution().reverseVowels('ai')

