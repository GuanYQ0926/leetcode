# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        nodelist = []
        current_node = head
        while current_node is not None:
            nodelist.append(current_node)
            current_node = current_node.next
        if n == len(nodelist):
            return head.next
        else:
            nodelist[-n - 1].next = nodelist[-n].next
            return head
