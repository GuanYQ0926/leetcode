# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        val_list = []
        current = head
        while current:
            val_list.append(current.val)
            current = current.next
        val_list = sorted(val_list)
        node_list = []
        for i in val_list:
            node_list.append(ListNode(i))
        l = len(node_list)
        for i in xrange(l - 1):
            node_list[i].next = node_list[i + 1]
        return node_list[0]
