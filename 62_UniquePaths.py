class Solution(object):

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        count = [[1 for i in xrange(n)] for j in xrange(m)]
        for i in xrange(1, m):
            for j in xrange(1, n):
                count[i][j] = count[i - 1][j] + count[i][j - 1]
        return count[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.uniquePaths(2, 2))
