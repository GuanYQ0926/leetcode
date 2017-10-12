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
            return max(nums[0] + nums[2], nums[1])
        result = [0 for _ in xrange(len(nums))]
        result[0] = nums[0]
        result[1] = nums[1]
        result[2] = nums[0] + nums[2]
        cur_index = 3
        while cur_index < l:
            result[cur_index] = max(
                result[cur_index - 2], result[cur_index - 3]) + nums[cur_index]
            cur_index += 1
        return max(result[-1], result[-2])


if __name__ == '__main__':
    solution = Solution()
    print(solution.rob([1, 1, 1, 1]))
