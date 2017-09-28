class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        l = len(nums)
        nums = sorted(nums)
        index = 0
        while True:
            if index != l - 1 and nums[index] == nums[index + 1]:
                index += 2
            else:
                return nums[index]
