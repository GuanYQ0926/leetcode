# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        else:
            depth = 1
            res = []
            node_list = [root]
            while node_list:
                temp_res = []
                temp_node_list = []
                if depth % 2 != 0:
                    for node in node_list:
                        temp_res.append(node.val)
                        if node.left:
                            temp_node_list.append(node.left)
                        if node.right:
                            temp_node_list.append(node.right)
                else:
                    for node in node_list:
                        temp_res.append(node.val)
                        if node.right:
                            temp_node_list.append(node.right)
                        if node.left:
                            temp_node_list.append(node.left)
                node_list = list(reversed(temp_node_list))
                res.append(temp_res)
                depth += 1
            return res
