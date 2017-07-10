class Solution(object):

    def isValid(self, s):
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

    def allParenthesis(self, n, ps):
        '''
        ps init '('
        '''
        if n == 1:
            return ps
        else:
            temp_p = []
            for i in '()':
                for p in ps:
                    temp_p.append(p + i)
            num = n - 1
            allp = temp_p
            return self.allParenthesis(num, allp)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        re = []
        all_ps = self.allParenthesis(2 * n, ['('])
        for p in all_ps:
            if self.isValid(p):
                re.append(p)
        return re


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(3))
