class Solution(object):

    def process(self, res):
        if '-' not in res and '+' not in res and '*' not in res:
            if res not in self.results:
                self.results.append(res)
        else:
            for i in xrange(len(res)):
                if res[i] == '-' or res[i] == '+' or res[i] == '*':
                    temp = '(' + res[i - 1] + res[i] + res[i + 1] + ')'
                    self.process(res[:i - 1] + [temp] + res[i + 2:])

    def diffWaysToCompute(self, inp):
        """
        :type input: str
        :rtype: List[int]
        """
        self.formula = []
        self.results = []
        for i in xrange(len(inp)):
            if i == 0:
                temp = inp[i]
            else:
                if inp[i] == '-' or inp[i] == '+' or inp[i] == '*':
                    self.formula.append(temp)
                    self.formula.append(inp[i])
                    temp = ''
                else:
                    temp += inp[i]
        self.formula.append(temp)
        self.process(self.formula)
        return [eval(i[0]) for i in self.results]


if __name__ == '__main__':
    solution = Solution()
    solution.diffWaysToCompute("2*3-4*5")
