# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        val_list = []
        current = head
        while current:
            val_list.append(current.val)
            current = current.next
        return val_list == val_list[::-1]
