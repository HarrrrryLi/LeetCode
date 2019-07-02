class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort()
        size = len(intervals)
        for cnt in range(1, size):
            if intervals[cnt][0] < intervals[cnt - 1][1]:
                return False

        return True
