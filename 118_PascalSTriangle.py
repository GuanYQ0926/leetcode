class Solution(object):

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            res = [[1], [1, 1]]
            for num in xrange(3, numRows + 1):
                temp = [1] * num
                prev = res[num - 2]
                for i in xrange(1, len(prev)):
                    temp[i] = prev[i - 1] + prev[i]
                res.append(temp)
            return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.generate(6))
