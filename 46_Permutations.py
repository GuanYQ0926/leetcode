class Solution(object):

    def generatePermute(self, nums, res):
        if not nums:
            self.final_res.append(res)
            # return final_res
        else:
            for i in xrange(len(nums)):
                # res.append(nums[i])
                temp_nums = nums[:i] + nums[i + 1:]
                self.generatePermute(temp_nums, res + [nums[i]])

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.final_res = []
        self.generatePermute(nums, [])
        return self.final_res


if __name__ == '__main__':
    solution = Solution()
    print(solution.permute([]))
