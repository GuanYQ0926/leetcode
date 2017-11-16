class Solution(object):

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = sorted(nums)
        for i in xrange(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
