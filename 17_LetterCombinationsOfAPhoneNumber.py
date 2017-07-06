class Solution(object):

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num_chars = {'2': 'abc', '3': 'def', '4': 'ghi',
                     '5': 'jkl', '6': 'mno', '7': 'pqrs',
                     '8': 'tuv', '9': 'wxyz', '0': ' '}
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return [i for i in num_chars[digits[0]]]
        else:
            res = [i for i in num_chars[digits[0]]]
            prev_res = res
            next_res = []
            for digit in digits[1:]:
                for i in xrange(len(prev_res)):
                    for c in num_chars[digit]:
                        next_res.append(prev_res[i] + c)
                prev_res = next_res
                next_res = []
            return prev_res


if __name__ == '__main__':
    solution = Solution()
    print(len(solution.letterCombinations('234')))
