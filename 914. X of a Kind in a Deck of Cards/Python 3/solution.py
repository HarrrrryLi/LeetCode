class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        Cnter = collections.Counter(deck)
        X = Cnter[deck[0]]
        for key in Cnter:
            X = math.gcd(X, Cnter[key])

        return X >= 2
