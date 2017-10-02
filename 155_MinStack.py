class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_val = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.min_val is None or x < self.min_val:
            self.min_val = x

    def pop(self):
        """
        :rtype: void
        """
        if self.stack[-1] == self.min_val:
            self.stack.pop(-1)
            self.min_val = min(self.stack) if self.stack else None
        else:
            self.stack.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_val
