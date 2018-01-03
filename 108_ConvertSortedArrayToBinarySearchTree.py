# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums:
            ind = len(nums) / 2
            root = TreeNode(nums[ind])
            root.left = self.sortedArrayToBST(nums[:ind])
            root.right = self.sortedArrayToBST(nums[ind + 1:])
            return root
