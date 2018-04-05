class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if len(haystack) == 0 and len(needle) == 0:
            return 0

        if len(haystack) == 0 or len(needle) == 0:
            return -1

        ind = -1

        for i in range(len(haystack) - len(needle)):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1