class Solution(object):

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        if l == 1:
            return nums[0]
        if l == 2:
            return max(nums[0], nums[1])
        if l == 3:
            return max(nums[0], nums[1], nums[2])
        cur_index, res = 3, [0 for _ in xrange(len(nums) - 1)]
        res[0], res[1], res[2] = nums[0], nums[1], nums[0] + nums[2]
        while cur_index < l - 1:
            res[cur_index] = max(res[cur_index - 2],
                                 res[cur_index - 3]) + nums[cur_index]
            cur_index += 1
        print(res)

        nums[0] = 0
        cur_index, res1 = 3, [0 for _ in xrange(len(nums))]
        res1[0], res1[1], res1[2] = nums[0], nums[1], nums[0] + nums[2]
        while cur_index < l:
            res1[cur_index] = max(res1[cur_index - 2],
                                  res1[cur_index - 3]) + nums[cur_index]
            cur_index += 1
        print(res1)
        return max(res[-1], res[-2], res1[-1], res1[-2])


if __name__ == '__main__':
    solution = Solution()
    print solution.rob([1, 2, 1, 1])
