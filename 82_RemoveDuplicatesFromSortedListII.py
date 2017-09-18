class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        current = head
        prev_val = None
        nodelist = []
        trigger = True
        while current:
            if prev_val == current.val:
                if trigger:
                    nodelist.pop(-1)
                    trigger = False
            else:
                trigger = True
                nodelist.append(current)
                prev_val = current.val
            current = current.next

        if not nodelist:
            return None
        else:
            for i in xrange(len(nodelist) - 1):
                print(nodelist[i].val)
                nodelist[i].next = nodelist[i + 1]
            nodelist[len(nodelist) - 1].next = None
            return nodelist[0]


if __name__ == '__main__':
    a, b, c = ListNode(1), ListNode(2), ListNode(2)
    a.next = b
    b.next = c
    solution = Solution()
    solution.deleteDuplicates(a)
