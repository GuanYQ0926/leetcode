class Solution(object):

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        else:
            row = len(grid)
            col = len(grid[0])
            count = [[0 for c in xrange(col)] for r in xrange(row)]
            init_val = 0
            for c in xrange(col):
                init_val += grid[0][c]
                count[0][c] = init_val
            init_val = 0
            for r in xrange(row):
                init_val += grid[r][0]
                count[r][0] = init_val
            for r in xrange(1, row):
                for c in xrange(1, col):
                    count[r][c] = min(
                        count[r - 1][c], count[r][c - 1]) + grid[r][c]
            return count[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print solution.minPathSum([[1]])
