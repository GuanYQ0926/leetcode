class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return digits
        flag, length = 1, len(digits)
        for i in range(len(digits)):
            ii = length - 1 - i
            n = digits[ii]
            if n == 9 and flag == 1:
                digits[ii], flag = 0, 1
            else:
                digits[ii] = n + flag
                flag = 0
                break
        if flag == 1:
            return ([1] + digits)
        return digits
