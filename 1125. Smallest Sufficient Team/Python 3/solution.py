class Solution:
    def smallestSufficientTeam(self, req_skills: list[str], people: list[list[str]]) -> list[int]:
        size = len(req_skills)
        skill_dict = dict()
        for idx, skill in enumerate(req_skills):
            skill_dict[skill] = idx

        dp = {0: []}

        for idx, person in enumerate(people):
            pskill = 0
            for skill in person:
                if skill in skill_dict:
                    pskill |= 1 << skill_dict[skill]

            for skills, team in list(dp.items()):
                with_curr = skills | pskill
                if skills == with_curr:
                    continue

                if with_curr not in dp or len(dp[with_curr]) > len(team) + 1:
                    dp[with_curr] = team + [idx]
            # print(dp)

        return dp[(1 << size) - 1]
