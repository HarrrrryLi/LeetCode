class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        result = 0
        while people:
            num1 = people[0]
            result += 1
            people.pop(0)
            if 2 * num1 <= limit and people:
                idx = bisect.bisect_right(people, limit - num1)
                if idx == len(people):
                    people.pop(-1)
                elif idx > 0:
                    people.pop(idx - 1)

        return result
