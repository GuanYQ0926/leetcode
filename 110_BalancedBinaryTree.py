# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            if root.right and root.left:
                return self.isBalanced(root.right) and self.isBalanced(root.left)
            elif root.right and (not root.left):
                if root.right.right or root.right.left:
                    return False
                else:
                    return True
            elif root.left and (not root.right):
                if root.left.right or root.left.left:
                    return False
                else:
                    return True
            else:
                return True
        else:
            return True
