class Solution(object):

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        results = []
        temp = []
        x = 1
        while True:
            l = len(temp)
            if l == k:
                results.append(temp[:])
            if l == k or x > n - k + l + 1:
                if not temp:
                    return results
                else:
                    x = temp.pop() + 1
            else:
                temp.append(x)
                x += 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.combine(4, 2))
