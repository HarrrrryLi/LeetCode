class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.memory = set()

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            self.memory.add(word)

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        size = len(word)
        for c in 'abcdefghijklmnopqrstuvwxyz':
            for idx in range(size):
                if c == word[idx]:
                    continue
                if word[:idx] + c + word[idx + 1:] in self.memory:
                    return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
