class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        l = 0
        r = 0
        already_parsed = {}
        substring_lengths = []

        while r < len(s):
            print l, r

            if s[r] not in already_parsed:
                already_parsed[s[r]] = r

            elif s[r] == s[l]:
                l += 1
                already_parsed[s[r]] = r

            else:
                substring_lengths.append(r - l)
                while l < already_parsed[s[r]]:
                    del already_parsed[s[l]]
                    l += 1
                l += 1
                already_parsed[s[r]] = r
            r += 1

        if len(substring_lengths) == 0:
            return (r - l)
        else:
            return max(r - l, max(substring_lengths))

print Solution().lengthOfLongestSubstring("ruowzgiooobpple")