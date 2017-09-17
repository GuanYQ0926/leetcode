class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        current = head
        nodelist = []
        while current:
            nodelist.append(ListNode(current.val))
            current = current.next
        nodelist = nodelist[:m - 1] + \
            list(reversed(nodelist[m - 1:n])) + nodelist[n:]
        for i in xrange(len(nodelist) - 1):
            nodelist[i].next = nodelist[i + 1]
        current = nodelist[0]
        while current:
            print(current.val)
            current = current.next
        return nodelist[0]


if __name__ == '__main__':
    a, b, c, d, e, f = ListNode(1), ListNode(
        2), ListNode(3), ListNode(4), ListNode(5), ListNode(6)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    solution = Solution()
    solution.reverseBetween(a, 1, 6)
