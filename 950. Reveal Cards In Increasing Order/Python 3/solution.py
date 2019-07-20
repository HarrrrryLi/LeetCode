class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        return self.helper(deck)

    def helper(self, deck):
        size = len(deck)
        if size == 1:
            return deck
        if size == 2:
            return deck

        result = [0] * size
        if size % 2 == 1:
            mid = size // 2 + 1
            result[::2] = deck[:mid]
            temp = self.deckRevealedIncreasing(deck[mid:])
            last = temp.pop()
            temp.insert(0, last)
            result[1::2] = temp
        else:
            mid = size // 2
            result[::2] = deck[:mid]
            result[1::2] = self.deckRevealedIncreasing(deck[mid:])

        return result
