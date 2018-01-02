class Solution(object):

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        self.tokens = tokens[:]
        indice = 0
        while len(self.tokens) != 1:
            char = self.tokens[indice]
            if char == '+':
                temp = float(self.tokens[indice - 2]) + \
                    float(self.tokens[indice - 1])
                self.tokens[indice - 2] = str(int(temp))
                self.tokens.pop(indice)
                self.tokens.pop(indice - 1)
                indice -= 1
            elif char == '-':
                temp = float(self.tokens[indice - 2]) - \
                    float(self.tokens[indice - 1])
                self.tokens[indice - 2] = str(int(temp))
                self.tokens.pop(indice)
                self.tokens.pop(indice - 1)
                indice -= 1
            elif char == '*':
                temp = float(self.tokens[indice - 2]) * \
                    float(self.tokens[indice - 1])
                self.tokens[indice - 2] = str(int(temp))
                self.tokens.pop(indice)
                self.tokens.pop(indice - 1)
                indice -= 1
            elif char == '/':
                temp = float(self.tokens[indice - 2]) / \
                    float(self.tokens[indice - 1])
                self.tokens[indice - 2] = str(int(temp))
                self.tokens.pop(indice)
                self.tokens.pop(indice - 1)
                indice -= 1
            else:
                indice += 1
        return int(self.tokens[0])


if __name__ == '__main__':
    test1 = ["10", "6", "9", "3", "+", "-11",
             "*", "/", "*", "17", "+", "5", "+"]
    test2 = ['0', '3', '/']
    solution = Solution()
    print(solution.evalRPN(test1))
