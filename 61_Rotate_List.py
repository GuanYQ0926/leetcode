# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        else:
            array = []
            cur = head
            while cur:
                array.append(cur)
                cur = cur.next
            k = k % len(array)
            if k == 0 or len(array) == 1:
                return array[0]
            else:
                node1, node2 = array[-k], array[-1]
                node3 = array[-k - 1]
                node2.next = array[0]
                node3.next = None
                return node1
