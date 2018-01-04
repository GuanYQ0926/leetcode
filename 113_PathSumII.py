# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def pathSum(self, root, Sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []

        def func(root, Sum, path):
            if not root:
                return
            if not root.left and not root.right and root.val == Sum:
                res.append(path + [root.val])
                return
            func(root.left, Sum - root.val, path + [root.val])
            func(root.right, Sum - root.val, path + [root.val])
        func(root, Sum, [])
        return res
