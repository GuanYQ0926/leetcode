class Solution(object):

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1 = 0
        index2 = len(numbers) - 1
        while True:
            temp = numbers[index1] + numbers[index2]
            if temp == target:
                return [index1 + 1, index2 + 1]
            elif temp > target:
                index2 = index2 - 1
            else:
                index1 += 1
