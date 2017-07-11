# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        elif head.next is None:
            return head
        else:
            result = head.next
            count = 1
            current = head
            temp = head
            pprev = head
            while current is not None:
                if count % 2 == 0:
                    temp.next = current.next
                    current.next = temp
                    if count > 3:
                        pprev.next = current
                        pprev = temp
                else:
                    temp = current
                current = temp.next
                count += 1
            return result


if __name__ == '__main__':
    head, node2, node3, node4, node5, node6 = ListNode(
        1), ListNode(2), ListNode(3), ListNode(4), ListNode(5), ListNode(6)
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    solution = Solution()
    result = solution.swapPairs(head)
    print('=========================')
    while result is not None:
        print(result.val)
        result = result.next
