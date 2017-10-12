# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        node_list = [root]
        temp_node_list = []
        result = [root.val]
        while True:
            for node in node_list:
                if node.left:
                    temp_node_list.append(node.left)
                if node.right:
                    temp_node_list.append(node.right)
            if temp_node_list:
                result.append(temp_node_list[-1].val)
                node_list = temp_node_list[:]
                temp_node_list = []
            else:
                break
        return result
