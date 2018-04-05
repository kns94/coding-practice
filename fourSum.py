class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        
        hm = {}

        for i in range(len(A)):
            for j in range(len(B)):
                hm.setdefault((A[i] + B[j]), 0)
                hm[(A[i] + B[j])] += 1

        zeroSum = 0
        for i in range(len(C)):
            for j in range(len(D)):
                if -(C[i] + D[j]) in hm:
                    zeroSum += hm[-(C[i] + D[j])]

        return zeroSum