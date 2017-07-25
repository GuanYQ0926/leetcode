class Solution(object):

    def twoSum(self, temp_i, temp_t, res):
        i = temp_i
        j = temp_t - i
        while i <= j:
            if j in self.candidates and (i in self.candidates or i == 0):
                if i == 0:
                    self.results.append(res + [j])
                else:
                    self.results.append(res + [i, j])
                    self.twoSum(i, j, res + [i])
            if i in self.candidates and j not in self.candidates:
                self.twoSum(i, j, res + [i])
            j -= 1
            i += 1

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.candidates = []
        self.results = []
        self.candidates = sorted(candidates)
        self.twoSum(0, target, [])
        return self.results


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum([1, 2], 4))
