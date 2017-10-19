class Solution(object):

    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        d = n - m
        if d == 0:
            return m
        p = 0
        while d:
            p += 1
            d >>= 1
        return ((m & n) >> p) << p


if __name__ == '__main__':
    solution = Solution()
    print solution.rangeBitwiseAnd(2, 3)
