class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        res = matrix[:]
        for i, row in enumerate(matrix):
            if 0 in row:
                res[i] = [0] * len(row)
                print('in')
        temp = list(map(list, zip(*matrix)))
        res = list(map(list, zip(*res)))
        for i, row in enumerate(temp):
            if 0 in row:
                res[i] = [0] * len(row)
        res = list(map(list, zip(*res)))
        for i in range(len(res)):
            for j in range(len(res[0])):
                matrix[i][j] = res[i][j]


if __name__ == '__main__':
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    solution = Solution()
    solution.setZeroes(matrix)
