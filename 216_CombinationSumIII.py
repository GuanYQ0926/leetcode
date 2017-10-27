class Solution(object):

    def dfs(self, k, start, target, temp):
        if k == 2:
            s, e = start, target - start
            while e > s:
                if e <= 9 and temp + [s, e] not in self.res:
                    self.res.append(temp + [s, e])
                e -= 1
                s += 1
        else:
            for i in xrange(1, 10 - start):
                self.dfs(k - 1, start + i, target - start, temp + [start])

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.res = []
        for i in xrange(1, n - k + 2):
            self.dfs(k, i, n, [])
        return self.res


if __name__ == '__main__':
    solution = Solution()
    print solution.combinationSum3(4, 24)
