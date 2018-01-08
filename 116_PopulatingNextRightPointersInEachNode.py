# Definition for binary tree with next pointer.
class TreeLinkNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing

    def connect(self, root):
        def func(cur):
            if not cur:
                return None
            pre = None
            first = cur.left
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                    if pre:
                        pre.right.next = cur.left
                    pre = cur
                    cur = cur.next
                else:
                    break
            return func(first)

        func(root)
