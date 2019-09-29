class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        splited = []
        d = collections.defaultdict(list)
        for idx, phrase in enumerate(phrases):
            words = phrase.split(' ')
            d[words[0]].append((words, idx))
            splited.append(words)

        result = set()
        for idx, words in enumerate(splited):
            if words[-1] in d:
                for nxt, i in d[words[-1]]:
                    if i != idx:
                        result.add(' '.join(words + nxt[1:]))

        return sorted(result)
