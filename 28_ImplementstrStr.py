class Solution(object):

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        elif needle and not haystack:
            return -1
        else:
            needle_len = len(needle)
            haystack_len = len(haystack)
            for i in xrange(len(haystack)):
                if haystack[i] == needle[0] and haystack_len - i >= needle_len:
                    if haystack[i:i + needle_len] == needle:
                        return i
            return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.strStr("mississippi", "issip"))
