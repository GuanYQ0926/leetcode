class Solution(object):

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # [[0,1],[-1,0]] | x'=y y'=-x
        row, col = len(matrix), len(matrix[0])
        # if(row == 1):
        #     return
        results = [[0] * col for _ in xrange(row)]
        for r in xrange(row):  # y
            for c in xrange(col):  # x
                # x, y = col - (r + 1), c + 1
                # results[y - 1][x] = matrix[r][c]
                results[c][-r - 1] = matrix[r][c]
        for i in xrange(row):
            for j in xrange(col):
                matrix[i][j] = results[i][j]
        return


if __name__ == '__main__':
    solution = Solution()
    matrix = [[1, 2], [3, 4]]
    solution.rotate(matrix)
    print(matrix)
