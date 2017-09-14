class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        else:
            nums = []
            for rows in matrix:
                nums += rows
            start = 0
            end = len(nums) - 1
            while start <= end:
                mid = (start + end) / 2
                if target == nums[mid]:
                    return True
                elif target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchMatrix([[1,   3,  5,  7],
                                 [10, 11, 16, 20],
                                 [23, 30, 34, 50]], 3))
