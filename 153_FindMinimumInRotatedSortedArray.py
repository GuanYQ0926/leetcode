class Solution(object):

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        prev = nums[0]
        for num in nums[1:]:
            if num < prev:
                if num < res:
                    res = num
                break
            else:
                prev = num
        return res
