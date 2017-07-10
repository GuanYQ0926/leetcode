class Solution(object):

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()
        for i in xrange(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in xrange(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k, l = j + 1, len(nums) - 1
                while l > k:
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        k += 1
                        continue
                    if l < len(nums) - 1 and nums[l] == nums[l + 1]:
                        l -= 1
                        continue
                    temp_s = nums[i] + nums[j] + nums[k] + nums[l]
                    if temp_s == target:
                        results.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                    elif temp_s < target:
                        k += 1
                    else:
                        l -= 1
        return results


if __name__ == '__main__':
    solution = Solution()
    # print(solution.fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0))
    print(solution.fourSum([0, 0, 0, 0], 0))
