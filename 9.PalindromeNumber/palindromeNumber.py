class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # x = str(x)
        # return x == x[::-1]
        if x < 0:
            return False
        num_str = str(x)
        num_len = len(num_str)
        if num_len == 1:
            return True
        if num_len % 2:  # odd
            mid_indice = num_len / 2
            if num_str[:mid_indice] == num_str[mid_indice + 1:][::-1]:
                return True
            else:
                return False
        else:
            right_indice = num_len / 2
            if num_str[:right_indice] == num_str[right_indice:][::-1]:
                return True
            else:
                return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(-1331))
