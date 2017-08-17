def dfs(result, path, pos, nums):
    result.append(path[:])
    for i in range(pos, len(nums)):
        path.append(nums[i])
        dfs(result, path, i + 1, nums)
        path.pop()


def subsets(nums):
    result = []
    dfs(result, [], 0, nums)
    return result


if __name__ == '__main__':
    print(subsets([1, 2, 3, 4]))
