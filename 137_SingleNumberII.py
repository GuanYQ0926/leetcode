class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        nums = sorted(nums)
        i = 0
        while i < len(nums):
            if i == len(nums) - 1:
                return nums[i]
            if nums[i] == nums[i + 1]:
                i = i + 3
            else:
                return nums[i]


if __name__ == '__main__':
    solution = Solution()
    solution.singleNumber([2, 2, 3, 2])
