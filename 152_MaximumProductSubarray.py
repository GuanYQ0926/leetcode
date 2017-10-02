class Solution(object):

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        small = nums[0]
        big = nums[0]
        res = nums[0]
        for i in xrange(1, len(nums)):
            big1 = max(nums[i], nums[i] * big, nums[i] * small)
            small1 = min(nums[i], nums[i] * big, nums[i] * small)
            big, small = big1, small1
            res = max(res, big)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProduct([-4, -3, -2]))
