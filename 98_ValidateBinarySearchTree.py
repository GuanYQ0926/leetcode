# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def bstSearch(self, node):
        self.res.append(node.val)
        if node.left is not None:
            self.bstSearch(node.left)
        if node.right is not None:
            self.bstSearch(node.right)

    def isValidBST(self, root, lessthan=float('inf'),
                   largerthan=float('-inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # self.res = []
        # self.bstSearch(root)
        if not root:
            return True
        else:
            if root.val >= lessthan or root.val <= largerthan:
                return False
            return self.isValidBST(root.left, min(root.val, lessthan),
                                   largerthan) \
                and self.isValidBST(root.right,
                                    lessthan, max(root.val, largerthan))


if __name__ == '__main__':
    root = TreeNode(10)
    l = root.left = TreeNode(5)
    r = root.right = TreeNode(15)
    ll = l.left = TreeNode(3)
    lr = l.right = TreeNode(7)
    lll = ll.left = TreeNode(1)
    llr = ll.right = TreeNode(4)
    lrl = lr.left = TreeNode(6)
    lrr = lr.right = TreeNode(9)
    solution = Solution()
    solution.isValidBST(root)
    print(solution.res)
