class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:

        result = set()
        record = collections.defaultdict(list)

        for transaction in transactions:
            name, time, amount, city = transaction.split(',')
            idx = bisect.bisect(record[name], (int(time), int(amount), city))
            record[name].insert(idx, (int(time), int(amount), city))

        for people in record:
            for t, a, c in record[people]:
                if a > 1000:
                    result.add('{},{},{},{}'.format(people, t, a, c))

                left_idx = bisect.bisect(record[people], (t - 60, -1, ''))
                right_idx = bisect.bisect(
                    record[people], (t + 60, 2001, 'z' * 11))
                for cnt in range(left_idx, min(len(record[people]), right_idx + 1)):
                    time, amount, city = record[people][cnt]
                    if abs(time - t) <= 60 and city != c:
                        result.add('{},{},{},{}'.format(people, t, a, c))
                        result.add('{},{},{},{}'.format(
                            people, time, amount, city))

        return list(result)
