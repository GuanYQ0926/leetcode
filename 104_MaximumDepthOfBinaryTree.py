# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def goDeeper(self, node, d):
        if node.left:
            self.goDeeper(node.left, d + 1)
        else:
            if d > self.depth:
                self.depth = d
        if node.right:
            self.goDeeper(node.right, d + 1)
        else:
            if d > self.depth:
                self.depth = d

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            self.depth = 1
            self.goDeeper(root, 1)
            return self.depth
