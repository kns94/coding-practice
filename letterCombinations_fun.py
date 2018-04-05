"""Dial a number from keypad and return possible alphabetical combinations the number will generate"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if len(digits) == 0: return []
        
        mapping = {
            1: ['*'],
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z'],
            0: [' ']
        }

        digits = map(int, digits)

        return reduce(lambda acc, digit: [x + y for x in acc for y in mapping[digit]], digits, [''])

print Solution().letterCombinations('23')
