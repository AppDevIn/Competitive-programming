# 1288. Remove Covered Intervals
# https://leetcode.com/problems/remove-covered-intervals/

class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        intervals.sort(key=lambda x: (x[0], -x[1]))
        n = len(intervals)
        max = 0

        for interval in intervals:
            if interval[1] > max:
                max = interval[1]
            else:
                n -= 1

        return n


s = Solution()
print(s.removeCoveredIntervals([[1, 4], [3, 6], [2, 8]]))
print(s.removeCoveredIntervals([[1, 4], [2, 3]]))
print(s.removeCoveredIntervals([[3, 10], [4, 10], [5, 11]]))
print(s.removeCoveredIntervals([[1, 2], [1, 4], [3, 4]]))
print(s.removeCoveredIntervals(
    [[66672, 75156], [59890, 65654], [92950, 95965], [9103, 31953], [54869, 69855], [33272, 92693], [52631, 65356],
     [43332, 89722], [4218, 57729], [20993, 92876]]))
