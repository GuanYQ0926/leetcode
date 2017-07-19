class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        temp_res = 0
        res = -10e9
        for i in xrange(len(nums)):
            temp_res += nums[i]
            if temp_res > res:
                res = temp_res
            if temp_res < 0:
                temp_res = 0
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
