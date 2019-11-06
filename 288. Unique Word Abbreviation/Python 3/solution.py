class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.record = collections.defaultdict(set)
        for word in dictionary:
            self.record[self.__abbrev(word)].add(word)

    def isUnique(self, word: str) -> bool:
        abb = self.__abbrev(word)
        if not abb in self.record:
            return True

        if len(self.record[abb]) == 1 and word in self.record[abb]:
            return True

        return False

    def __abbrev(self, s):
        size = len(s)
        if size > 2:
            return s[0] + str(size - 2) + s[-1]
        return s


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
