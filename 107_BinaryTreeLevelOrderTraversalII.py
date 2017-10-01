# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        else:
            nodelist = [root]
            res = []
            while nodelist:
                temp_nodelist = []
                temp_res = []
                for node in nodelist:
                    temp_res.append(node.val)
                    if node.left:
                        temp_nodelist.append(node.left)
                    if node.right:
                        temp_nodelist.append(node.right)
                nodelist = temp_nodelist
                res.append(temp_res)
            return list(reversed(res))
