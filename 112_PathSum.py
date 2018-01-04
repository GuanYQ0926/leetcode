# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def hasPathSum(self, root, Sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right and root.val == Sum:
            return True
        Sum -= root.val
        return self.hasPathSum(root.left, Sum) or self.hasPathSum(root.right, Sum)
