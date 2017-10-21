class Solution(object):

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == len(t):
            return map(lambda i: s.index(i), s) == map(lambda i: t.index(i), t)
        else:
            return False
