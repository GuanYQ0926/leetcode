class Solution(object):

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        state = []
        while True:
            nums = [int(s) for s in str(n)]
            if nums[0] == 1 and nums[1:] == [0] * (len(nums) - 1):
                return True
            nums = sorted(nums)
            if nums in state:
                return False
            else:
                state.append(nums)
            n = 0
            for num in nums:
                n += num**2
