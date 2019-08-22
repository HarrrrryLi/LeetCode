class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        size = len(tree)
        record = {}
        result = 0

        total = 0
        for idx, fruit in enumerate(tree):
            if fruit not in record:
                if len(record) == 2:
                    result = max(result, total)
                    cnt = idx - 1
                    while tree[cnt] == tree[idx - 1]:
                        cnt -= 1

                    for key in record:
                        if key != fruit and key != tree[idx - 1]:
                            del record[key]
                            break

                    record[tree[idx - 1]] = idx - 1 - cnt
                    record[fruit] = 1
                    total = idx - 1 - cnt + 1

                else:
                    record[fruit] = 1
                    total += 1
            else:
                record[fruit] += 1
                total += 1

        result = max(result, total)

        return result
