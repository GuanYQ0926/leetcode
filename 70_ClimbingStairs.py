class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n < 0:
        #     return 0
        # elif n == 0:
        #     return 1
        # else:
        #     return self.climbStairs(n - 2) + self.climbStairs(n - 1)
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            prev_count = 2
            pprev_count = 1
            for i in xrange(3, n + 1):
                temp = prev_count + pprev_count
                pprev_count = prev_count
                prev_count = temp
            return prev_count


if __name__ == '__main__':
    solution = Solution()
    print(solution.climbStairs(4))
