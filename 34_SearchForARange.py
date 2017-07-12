class Solution(object):

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        re1, re2 = -1, -1
        start_index, mid_index, end_index = 0, (len(
            nums) - 1) / 2, len(nums) - 1
        while start_index <= end_index:
            if target > nums[mid_index]:
                start_index = mid_index + 1
                mid_index = (start_index + end_index) / 2
            elif target < nums[mid_index]:
                end_index = mid_index - 1
                mid_index = (start_index + end_index) / 2
            else:
                re1 = re2 = mid_index
                while True:
                    if re1 - 1 >= 0 and nums[re1 - 1] == target:
                        re1 -= 1
                        continue
                    if re2 + 1 < len(nums) and nums[re2 + 1] == target:
                        re2 += 1
                        continue
                    break
                break
        return [re1, re2]


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchRange([2, 2], 3))
