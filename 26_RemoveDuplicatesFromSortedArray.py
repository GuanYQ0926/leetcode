class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        prev, length = nums[0], 1
        for num in nums[1:]:
            if num != prev:
                nums[length] = num
                length += 1
                prev = num
        return length


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicates([]))
