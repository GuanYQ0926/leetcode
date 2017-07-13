def twoSum(nums, target):
    nums_count = len(nums)
    for i in range(nums_count - 1):
        result = target - nums[i]
        try:
            index = nums.index(result)
            if index == i:
                continue
        except ValueError:
            continue
        else:
            return [i, index]


if __name__ == '__main__':
    print(twoSUm([3, 2, 4], 6))
