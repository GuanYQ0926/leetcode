# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def search(self, node, target, parents):
        if node == target:
            self.parents.append(parents)
        else:
            if node.left:
                self.search(node.left, target, parents + [node.left])
            if node.right:
                self.search(node.right, target, parents + [node.right])

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.parents = []
        self.search(root, p, [root])
        self.search(root, q, [root])
        a, b = self.parents[0], self.parents[1]
        print([i.val for i in a], [i.val for i in b])
        for i in reversed(self.parents[0]):
            for j in reversed(self.parents[1]):
                if i == j:
                    return i


if __name__ == '__main__':
    a, b, c, d, e, f, g, h, i = TreeNode(3), TreeNode(5), TreeNode(6),\
        TreeNode(2), TreeNode(7), TreeNode(4),\
        TreeNode(1), TreeNode(0), TreeNode(8)
    a.left = b
    a.right = g
    b.left = c
    b.right = d
    d.left = e
    d.right = f
    g.left = h
    g.right = i

    solution = Solution()
    parents = solution.lowestCommonAncestor(a, g, d)
