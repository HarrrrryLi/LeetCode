class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        hour = -1
        minute = -1

        for h1, h2, m1, m2 in itertools.permutations(A, 4):
            h = h1 * 10 + h2
            if h > 23:
                continue
            m = m1 * 10 + m2
            if m >= 60:
                continue

            if h > hour:
                hour = h
                minute = m
            elif h == hour:
                if m > minute:
                    hour = h
                    minute = m

        if hour == -1 or minute == -1:
            return ""

        return '{:02}:{:02}'.format(hour, minute)
