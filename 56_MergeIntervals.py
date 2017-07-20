# Definition for an interval.
class Interval(object):

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals
        res = []
        intervals.sort(key=lambda r: r.start)
        start = intervals[0].start
        end = intervals[0].end
        for i in xrange(1, len(intervals)):
            if intervals[i].start <= end:
                end = max(intervals[i].end, end)
            else:
                res.append(Interval(start, end))
                start = intervals[i].start
                end = intervals[i].end
        res.append(Interval(start, end))
        return res
