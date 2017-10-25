class Solution(object):

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # [1,2,3,4]
        results = []
        temp = 1
        for i in xrange(len(nums)):
            results.append(temp)
            temp *= nums[i]
        temp = 1
        for i in xrange(len(nums) - 1, -1, -1):
            results[i] *= temp
            temp *= nums[i]
        return results


if __name__ == '__main__':
    solution = Solution()
    print solution.productExceptSelf([1, 2, 3, 4])
