class Solution(object):

    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        allSwaps = [num]
        num = list(str(num))

        for i in range(len(num)):
            for j in range(len(num) - 1, i, -1):
                if num[i] < num[j]:
                    temp = num[:]
                    temp[i], temp[j] = temp[j], temp[i]
                    allSwaps += [int(''.join(temp))]

        return max(allSwaps)
        

num = 2736
print Solution().maximumSwap(num)