class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if len(nums) == 0 or len(nums) == 1:
            return nums

        if len(nums) == 2:
            return [nums, nums[::-1]]

        return self.recPermute(nums, [])

    def recPermute(self, nums, already_parsed):
        all_ind = set(range(len(nums)))
        remaining = list(all_ind - set(already_parsed))

        if len(remaining) == 1:
            return [nums[remaining[0]]]

        if len(remaining) == 2:
            c = [nums[remaining[0]], nums[remaining[1]]]
            return [c, c[::-1]]

        current = []
        for i in remaining:
            combs = self.recPermute(nums, already_parsed + [i])
            for c in combs:
                current += [[nums[i]] + c]
        return current

nums = [1, 2, 3, 4, 5]
print len(Solution().permute(nums))