class Solution(object):

    def unitAdd(self, carry, num1, num2):
        if carry == '1':
            if num1 == '1' and num2 == '1':
                carry, res = '1', '1'
            elif num1 == '0' and num2 == '0':
                carry, res = '0', '1'
            else:
                carry, res = '1', '0'
        else:
            if num1 == '1' and num2 == '1':
                carry, res = '1', '0'
            elif num1 == '0' and num2 == '0':
                carry, res = '0', '0'
            else:
                carry, res = '0', '1'
        return carry, res

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = '0'
        results = ''
        if len(a) > len(b):
            num1, num2 = a, b
        else:
            num1, num2 = b, a
        num_len = len(num1)
        num2 = '0' * (len(num1) - len(num2)) + num2
        for i in xrange(num_len - 1, -1, -1):
            carry, res = self.unitAdd(carry, num1[i], num2[i])
            results = res + results
        if carry == '1':
            results = carry + results
        return results  # return bin(int(a,2)+int(b,2))[2:]


if __name__ == '__main__':
    solution = Solution()
    print(solution.addBinary('1', '111'))
