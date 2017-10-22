# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        current = head
        val_list = []
        while current:
            val_list.append(current.val)
            current = current.next
        val_list = list(reversed(val_list))
        node_list = [ListNode(i) for i in val_list]
        cur = node_list[0]
        for i in node_list[1:]:
            cur.next = i
            cur = i
        return node_list[0]
