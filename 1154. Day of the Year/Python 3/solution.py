class Solution:
    def dayOfYear(self, date: str) -> int:
        m2d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        year, month, day = date.split('-')
        year, month, day = int(year), int(month), int(day)

        if year % 100:
            if not year % 4:
                m2d[1] = 29
        else:
            if not year % 400:
                m2d[1] = 29

        result = 0

        for cnt in range(month - 1):
            result += m2d[cnt]

        result += day

        return result
