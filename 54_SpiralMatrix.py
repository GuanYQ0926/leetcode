class Solution(object):

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        res = []
        count = 1
        while len(matrix) != 0 and len(matrix[0]) != 0:
            if count % 2 != 0:
                row_array = matrix[0]
                matrix = matrix[1:]
                col_array = [i[-1] for i in matrix]
                matrix = [i[:-1] for i in matrix]
            else:
                row_array = matrix[-1][::-1]
                matrix = matrix[:-1]
                col_array = [i[0] for i in matrix][::-1]
                matrix = [i[1:] for i in matrix]
            res += (row_array + col_array)
            count += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.spiralOrder([[1], [2], [3]]))
