class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []
        i = 0

        while i < len(s):
            if s[i] != ']':
                stack += [s[i]]
            else:
                string = []
                ele = stack.pop()

                while ele != '[':
                    #Everything inside bracket is saved to string
                    string += [ele]
                    ele = stack.pop()

                string =  ''.join(string[::-1])
                ele = stack.pop()
                number = ele

                while ele.isdigit() and len(stack) != 0:
                    #Get the number
                    ele = stack.pop()
                    if ele.isdigit():
                        number += ele
                    else:
                        stack += [ele]

                number = number[::-1]
                stack += [string * int(number)]
            i += 1

        return ''.join(stack)

s = "3[a]2[bc]"
#s = "3[a2[c]]"
s = "2[abc]3[cd]ef"
#s = "100[leetcode]"
#s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
print Solution().decodeString(s)
