class Solution(object):

    def combination(self, n, nums, reserved):
        if n == 1:
            res = []
            for i in nums:
                if [i] not in res:
                    res.append([i])
            return res
        elif n == 2:
            res = []
            used_list1 = []
            for i in xrange(len(nums) - 1):
                used_list2 = []
                if nums[i] not in used_list1:
                    used_list1.append(nums[i])
                    for j in xrange(i + 1, len(nums)):
                        if nums[j] not in used_list2:
                            used_list2.append(nums[j])
                            res.append([nums[i], nums[j]])
            return res
        else:
            # reserved = self.combination(n - 1, nums)
            res = []
            for temp in reserved:
                used_list = []
                index = nums.index(temp[-1])
                offset = -1
                for e in reversed(temp):
                    if e == temp[-1]:
                        offset += 1
                index += offset
                if index != len(nums) - 1:
                    for i in xrange(index + 1, len(nums)):
                        if nums[i] not in used_list:
                            used_list.append(nums[i])
                            res.append(temp + [nums[i]])
            return res

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        else:
            nums.sort()
            res = [[]]
            reserved = []
            for i in xrange(1, len(nums) + 1):
                reserved = self.combination(i, nums, reserved)
                res += reserved
            return res


if __name__ == '__main__':
    solution = Solution()
    print solution.subsetsWithDup([1, 1, 2, 2])
