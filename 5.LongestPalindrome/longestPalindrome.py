class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''
        elif len(s) == 1:
            return s
        elif len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[1]
        else:
            mid_indice = 1
            left_indice = mid_indice - 1
            right_indice = mid_indice + 1
            str_len = len(s)
            result = ''
            temp_result = s[mid_indice]
            while True:
                if left_indice >= 0 and s[left_indice] == s[mid_indice] and \
                        s[left_indice] == s[left_indice + 1]:
                    temp_result = s[left_indice] + temp_result
                    left_indice -= 1
                    continue
                if right_indice < str_len and \
                    s[right_indice] == s[mid_indice] and\
                        s[right_indice] == s[right_indice - 1]:
                    temp_result = temp_result + s[right_indice]
                    right_indice += 1
                    continue
                if left_indice >= 0 and right_indice < str_len and \
                        s[left_indice] == s[right_indice]:
                    temp_result = s[left_indice] + \
                        temp_result + s[right_indice]
                    left_indice -= 1
                    right_indice += 1
                # else: fail
                if left_indice < 0 or right_indice >= str_len or\
                        s[left_indice] != s[right_indice]:
                    if len(temp_result) >= len(result):
                        result = temp_result
                    mid_indice += 1
                    left_indice = mid_indice - 1
                    right_indice = mid_indice + 1
                    temp_result = s[mid_indice]
                if mid_indice >= str_len - 1:
                    break
            return result


if __name__ == '__main__':
    solution = Solution()
    print(len(solution.longestPalindrome('321012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210123210012321001232100123210123')))
