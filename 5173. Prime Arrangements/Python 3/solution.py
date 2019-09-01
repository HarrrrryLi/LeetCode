class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        prime_cnt = 0
        result = 0
        for num in range(2, n + 1):
            if self.isPrime(num):
                prime_cnt += 1

        result = self.permutations(prime_cnt) * \
            self.permutations(n - prime_cnt)

        return result % (10 ** 9 + 7)

    def permutations(self, n):
        result = 1
        for num in range(n, 1, -1):
            result *= num

        return result

    def isPrime(self, n):
        if n == 1 or n == 0:
            return False

        for num in range(2, int(math.sqrt(n)) + 1):
            if n % num == 0:
                return False

        return True
