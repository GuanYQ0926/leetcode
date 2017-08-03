class Solution(object):

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = s.split(' ')
        count = -1
        while count >= -len(temp):
            res = temp[count]
            if res:
                return len(res)
            count -= 1
        return 0


if __name__ == '__main__':
    solution = Solution()
    print solution.lengthOfLastWord('a ')
