class Solution(object):

    def canJump(self, nums):
        last = len(nums) - 1
        for i in xrange(len(nums) - 2, -1, -1):
            if i + nums[i] >= last:
                last = i
        return (last <= 0)


if __name__ == '__main__':
    solution = Solution()  # [3,2,1,0,4], [2, 3, 1, 1, 4]
    print(solution.canJump([3, 2, 1, 0, 4]))
