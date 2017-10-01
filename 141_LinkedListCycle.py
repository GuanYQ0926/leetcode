# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        current = head
        lead = head
        while current and lead and lead.next:
            current = current.next
            lead = lead.next.next
            if current == lead:
                return True
        return False
