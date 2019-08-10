class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        vrecord = collections.defaultdict(list)
        record = collections.defaultdict(set)
        for user, time, website in zip(username, timestamp, website):
            idx = bisect.bisect(vrecord[user], (time, website))
            vrecord[user].insert(idx, (time, website))

        for user in vrecord:
            for (_, web1), (_, web2), (_, web3) in itertools.combinations(vrecord[user], 3):
                record[(web1, web2, web3)].add(user)

        result = []
        max_time = 0
        for key in record:
            freq = len(record[key])
            if freq > max_time:
                result = list(key)
                max_time = freq
            elif freq == max_time:
                result = min(list(key), result)

        return result
