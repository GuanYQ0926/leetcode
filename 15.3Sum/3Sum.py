class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        for i in xrange(len(nums) - 2):
            for j in xrange(i + 1, len(nums) - 1):
                for k in xrange(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp_re = [nums[i], nums[j], nums[k]]
                        temp_re.sort()
                        if temp_re not in results:
                            results.append(temp_re)
        return results


if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
