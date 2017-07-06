class Solution(object):

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = 99999
        diff = 99999
        nums.sort()
        for i in xrange(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                temp_diff = abs(s - target)
                if temp_diff < diff:
                    diff = temp_diff
                    res = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return target
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSumClosest([-1, 2, 1, -4], 1))
