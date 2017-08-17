class Solution(object):

    def onelen(self, l):
        res = []
        temp = []
        x = 0
        while True:
            tl = len(temp)
            if tl == l:
                res.append(temp[:])
            if tl == l or x > self.length - l + tl:
                if not temp:
                    return res
                else:
                    x = temp.pop() + 1
            else:
                temp.append(x)
                x += 1

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        if not nums:
            return result
        else:
            self.nums = nums
            self.length = len(nums)
            for l in xrange(1, self.length + 1):
                temp_res = self.onelen(l)
                for res in temp_res:
                    result.append([self.nums[i] for i in res])
            return result


'''
def dfs(result, path, pos, nums):
    result.append(path[:])
    for i in range(pos, len(nums)):
        path.append(nums[i])
        dfs(result, path, i + 1, nums)
        path.pop()


def subsets(nums):
    result = []
    dfs(result, [], 0, nums)
    return result
'''


if __name__ == '__main__':
    solution = Solution()
    print(solution.subsets([1, 2, 3]))
