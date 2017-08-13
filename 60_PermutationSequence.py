class Solution(object):

    def factorial(self, n):
        res = 1
        for i in xrange(1, n + 1):
            res *= i
        return res

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        result = ''
        nums = [str(i) for i in range(1, n + 1)]
        divi = k - 1
        for i in xrange(n - 1, 0, -1):
            temp_count = self.factorial(i)
            quotient = divi / temp_count
            remainder = divi % temp_count
            res = str(nums[quotient])
            result += res
            nums.remove(res)
            divi = remainder
        result += nums[0]
        return result


if __name__ == '__main__':
    solution = Solution()
    print (solution.getPermutation(3, 1))
