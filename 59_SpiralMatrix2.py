class Solution(object):

    def fillTopRightLine(self):
        self.res[self.did_tr][self.did_tr:self.did_tr +
                              self.size] = self.nums[:self.size]
        for j in xrange(self.size - 1):
            self.res[self.did_tr + j +
                     1][-(self.did_tr + 1)] = self.nums[self.size + j]
        self.nums = self.nums[self.size * 2 - 1:]
        self.size -= 1
        self.did_tr += 1

    def fillBotLeftLine(self):
        self.res[-(self.did_bl + 1)][self.did_bl:self.did_bl +
                                     self.size] = self.nums[:self.size][::-1]
        for j in xrange(self.size - 1):
            self.res[-(self.did_bl + 1 + j + 1)
                     ][self.did_bl] = self.nums[self.size + j]
        self.nums = self.nums[self.size * 2 - 1:]
        self.size -= 1
        self.did_bl += 1

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.did_tr = 0
        self.did_bl = 0
        self.size = n
        self.nums = range(1, n**2 + 1)
        self.res = [[0] * n for _ in xrange(n)]
        while self.nums:
            self.fillTopRightLine()
            if not self.nums:
                break
            self.fillBotLeftLine()
        return self.res


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateMatrix(0))
