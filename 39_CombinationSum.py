class Solution(object):

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        i, j = 0, len(candidates) - 1
        one = min_num = candinates[0]
        results = []
        if target in candidates:
            results.append([target])
        while i <= j:
            two = target - one
            if two in candidates:
