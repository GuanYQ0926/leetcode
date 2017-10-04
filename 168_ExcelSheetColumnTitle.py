class Solution(object):

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ''
        else:
            res = ''
            char_list = [chr(x) for x in xrange(ord('A'), ord('Z') + 1)]
            while n > 0:
                res = char_list[(n - 1) % 26] + res
                n = (n - 1) / 26
            return res


if __name__ == '__main__':
    solution = Solution()
    print solution.convertToTitle(701)
