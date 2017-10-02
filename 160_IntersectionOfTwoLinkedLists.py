# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        listA, listB = [], []
        currentA, currentB = headA, headB
        while currentA:
            listA.append(currentA.val)
            currentA = currentA.next
        while currentB:
            listB.append(currentB.val)
            currentB = currentB.next
        listA, listB = list(reversed(listA)), list(reversed(listB))
        listC = []
        for a, b in zip(listA, listB):
            if a == b:
                listC = [a] + listC
            else:
                break
        if not listC:
            return None
        res = ListNode(listC[0])
        currentC = res
        for c in listC[1:]:
            currentC.next = ListNode(c)
            currentC = currentC.next
        return res
