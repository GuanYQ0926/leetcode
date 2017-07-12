class Solution(object):

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result_dict = {}
        for i in strs:
            temp = ''.join(sorted(i))
            if temp in result_dict:
                result_dict[temp].append(i)
            else:
                result_dict[temp] = [i]
        results = [result_dict[i] for i in result_dict]
        return results


if __name__ == '__main__':
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
