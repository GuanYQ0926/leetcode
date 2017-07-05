class Solution(object):

    def isMatch(self, s, p):
        table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        table[0][0] = True
        for i in range(2, len(p) + 1):
            table[i][0] = table[i - 2][0] and p[i - 1] == '*'

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] != "*":
                    table[i][j] = table[i - 1][j - 1] and \
                        (p[i - 1] == s[j - 1] or p[i - 1] == '.')
                else:
                    table[i][j] = table[i - 2][j] or table[i - 1][j]
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        table[i][j] |= table[i][j - 1]

        return table[-1][-1]


if __name__ == '__main__':
    '''
    isMatch("aa","a") false
    isMatch("aa","aa") true
    isMatch("aaa","aa") false
    isMatch("aa", "a*") true
    isMatch("aa", ".*") true
    isMatch("ab", ".*") true
    isMatch("aab", "c*a*b") true
    "aaa", "ab*a*c*a" true
    "a", ".*..a*" false
    'ab', '.*..' true
    '''
    solution = Solution()
    print(solution.isMatch("a", ".*..a*"))
