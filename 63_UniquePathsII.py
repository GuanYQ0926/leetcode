class Solution(object):

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        if rows == 1 or cols == 1:
            for r in xrange(rows):
                for c in xrange(cols):
                    if obstacleGrid[r][c] == 1:
                        return 0
            return 1
        count = [[1 for i in xrange(cols)] for j in xrange(rows)]
        # first row
        for i in xrange(cols):
            if obstacleGrid[0][i] == 1:
                for j in xrange(i, cols):
                    count[0][j] = 0
                break
        # first col
        for i in xrange(rows):
            if obstacleGrid[i][0] == 1:
                for j in xrange(i, rows):
                    count[j][0] = 0
                break
        for r in xrange(1, rows):
            for c in xrange(1, cols):
                if obstacleGrid[r][c] == 1:
                    count[r][c] = 0
                if count[r][c] != 0:
                    count[r][c] = count[r - 1][c] + count[r][c - 1]
        return count[-1][-1]
