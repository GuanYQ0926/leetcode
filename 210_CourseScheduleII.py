import collections


class Solution(object):

    def dfs(self, node):
        if self.visited[node] == -1:
            return False
        if self.visited[node] == 1:
            return True
        self.visited[node] = -1
        for x in self.graph[node]:
            if not self.dfs(x):
                return False
        self.visited[node] = 1
        self.res.append(node)
        return True

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self.graph = collections.defaultdict(list)
        self.res = []
        for pair in prerequisites:
            self.graph[pair[0]].append(pair[1])
        self.visited = [0 for x in xrange(numCourses)]
        for x in xrange(numCourses):
            if not self.dfs(x):
                return []
        return self.res


if __name__ == '__main__':
    solution = Solution()
    print solution.findOrder(10, [[5, 8], [3, 5], [1, 9], [
        4, 5], [0, 2], [7, 8], [4, 9]])
