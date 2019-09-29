import datetime


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        day_list = ["Monday", "Tuesday", "Wednesday",
                    "Thursday", "Friday", "Saturday", "Sunday"]
        d = datetime.date(year, month, day)
        return day_list[d.weekday()]
