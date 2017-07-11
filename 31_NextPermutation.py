# class Solution(object):
#
#     def nextPermutation(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         num_array = sorted(nums)
#         num_array = num_array[::-1]
#         if num_array == nums:
#             nums = nums[::-1]
#             print('+++', nums)
#             return
#         else:
#             for i in xrange(len(nums) - 1, 0, -1):
#                 if nums[i] <= nums[i - 1]:
#                     continue
#                 else:
#                     if i + 1 == len(nums):
#                         nums[i - 1], nums[i] = nums[i], nums[i - 1]
#                     else:
#                         if nums[i - 1] > nums[i + 1]:  # left>right
#                             nums[i - 1], nums[i] = nums[i], nums[i - 1]
#                         else:  # left <= right
#                             nums[i - 1], nums[i + 1] = nums[i + 1], nums[i - 1]
#                     print(nums[:i], sorted(nums[i:]))
#                     nums = nums[:i] + sorted(nums[i:])
#                     print('===', nums)
#                     return
#             nums = nums[::-1]
#             print('---', nums)
#             return


class Solution(object):

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:   # nums are in descending order
            nums.reverse()
            return
        k = i - 1    # find the last "ascending" position
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        l, r = k + 1, len(nums) - 1  # reverse the second part
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


if __name__ == '__main__':
    solution = Solution()
    solution.nextPermutation([1, 3, 2])
