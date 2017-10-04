class Solution(object):

    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, i, res = len(s) - 1, 0, 0
        while l >= 0:
            res += (ord(s[i]) - ord('A') + 1) * 26**l
            i += 1
            l -= 1
        return res
