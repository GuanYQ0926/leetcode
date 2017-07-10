class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        stash = ''
        for i in s:
            if i == '(' or i == '{' or i == "[":
                stash += i
            else:
                if i == ')' and len(stash) > 0 and stash[-1] == '(':
                    stash = stash[:-1]
                elif i == '}' and len(stash) > 0 and stash[-1] == '{':
                    stash = stash[:-1]
                elif i == ']' and len(stash) > 0 and stash[-1] == '[':
                    stash = stash[:-1]
                else:
                    return False
        if len(stash) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid('()'))
