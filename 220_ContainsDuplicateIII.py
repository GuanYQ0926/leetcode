class Solution(object):

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        nums_list = []
        for i, v in enumerate(nums):
            nums_list.append([i, v])
        nums_list = sorted(nums_list, key=lambda x: x[1])

        for i in xrange(len(nums_list)):
