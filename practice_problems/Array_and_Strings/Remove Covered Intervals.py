class Solution(object):
    # Sort in the ascending order by the start point.
    # If two intervals share the same start point, put the longer one to be the first
    # Initiate the number of non-covered intervals: count = 0
    # Iterate over sorted intervals and compare end points
    # If the current interval is not covered by the previous one end > prev_end, increase the number of non-covered intervals
    # Assign the current interval to be previous for the next step
    # Otherwise, the current interval is covered by the previous one. Do nothing.
    # return count
    def removeCoveredIntervals(self, intervals):

        intervals.sort(key = lambda x : (x[0], -x[1]))

        count = 0
        prev_end = 0

        for _, end in intervals:
            if end > prev_end:
                count += 1
                prev_end = end
        return count