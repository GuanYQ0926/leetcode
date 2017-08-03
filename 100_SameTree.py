# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        else:
            parent_nodes1 = [p]
            parent_nodes2 = [q]
            child_nodes1 = []
            child_nodes2 = []
            while len(parent_nodes1) != 0 and len(parent_nodes2) != 0:
                for i, j in zip(parent_nodes1, parent_nodes2):
                    if i.val != j.val:
                        return False
                    else:
                        if i.left is not None and j.left is not None:
                            child_nodes1.append(i.left)
                            child_nodes2.append(j.left)
                        elif i.left is None and j.left is None:
                            pass
                        else:
                            return False
                        if i.right is not None and j.right is not None:
                            child_nodes1.append(i.right)
                            child_nodes2.append(j.right)
                        elif i.right is None and j.right is None:
                            pass
                        else:
                            return False
                parent_nodes1, parent_nodes2 = child_nodes1, child_nodes2
                child_nodes1 = []
                child_nodes2 = []
        return True


if __name__ == '__main__':
    p = TreeNode(0)
    p.left = TreeNode(-5)
    q = TreeNode(0)
    q.left = TreeNode(-8)
    solution = Solution()
    print(solution.isSameTree(p, q))
