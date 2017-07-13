class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        min_len_index = -1
        min_len = 100000
        for i in xrange(len(strs)):
            if len(strs[i]) < min_len:
                min_len_index = i
                min_len = len(strs[i])
        strs = strs[:min_len_index] + strs[min_len_index:]
        prefix = strs[min_len_index]
        while len(prefix) != 0:
            flag = True
            for i in strs:
                if i[:len(prefix)] != prefix:
                    flag = False
                    break
            if flag:
                return prefix
            else:
                prefix = prefix[:-1]
        return prefix


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(
        ['geeksforgeeks', 'geeks', 'geek', 'geezer']))
