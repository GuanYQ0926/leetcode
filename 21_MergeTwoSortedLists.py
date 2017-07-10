# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        if l1 is None and l2 is not None:
            return l2
        if l1 is not None and l2 is None:
            return l1
        nodel1, nodel2, res, curr = l1, l2, None, None
        if nodel1.val <= nodel2.val:
            res = curr = nodel1
            nodel1 = nodel1.next
        else:
            res = curr = nodel2
            nodel2 = nodel2.next
        while nodel1 is not None or nodel2 is not None:
            if nodel1 is not None and nodel2 is not None:
                if nodel1.val < nodel2.val:
                    curr.next = nodel1
                    curr = nodel1
                    nodel1 = nodel1.next
                else:
                    curr.next = nodel2
                    curr = nodel2
                    nodel2 = nodel2.next
            elif nodel1 is None and nodel2 is not None:
                curr.next = nodel2
                break
            else:
                curr.next = nodel1
                break
        return res
