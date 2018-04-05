class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidate_combinations = {}
        candidates = [c for c in candidates if c <= target]
        for candidate in candidates:
            current = []
            currentSum = 0
            while currentSum < target:
                current = current[:] + [candidate]
                currentSum += candidate
                candidate_combinations.setdefault(currentSum, [])
                candidate_combinations[currentSum] += [current]

        result = []
        print candidate_combinations
        for k, v in candidate_combinations.iteritems():
            if k == target:
                for c in candidate_combinations[k]:
                    if sorted(c) not in result:
                        result += [sorted(c)]

            if k < target:
                if target - k in candidate_combinations:
                    for c1 in candidate_combinations[k]:
                        for c2 in candidate_combinations[target - k]:
                            if sorted(c1 + c2) not in result:
                                result = result[:] + [sorted(c1 + c2)]

        return result

print Solution().combinationSum([7, 3, 2], 18)
        

