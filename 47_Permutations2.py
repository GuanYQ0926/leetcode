class Solution(object):

    def generatePermute(self, nums, res):
        if not nums:
            self.results.append(res)
        else:
            for i in xrange(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                else:
                    temp_nums = nums[:i] + nums[i + 1:]
                    self.generatePermute(temp_nums, res + [nums[i]])

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.results = []
        nums.sort()
        self.generatePermute(nums, [])
        return self.results


if __name__ == '__main__':
    solution = Solution()
    print(solution.permuteUnique([1]))
