# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        self.tree = None

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root:
            self.flatten(root.right)
            self.flatten(root.left)
            root.right = self.tree
            root.left = None
            self.tree = root
        else:
            return
