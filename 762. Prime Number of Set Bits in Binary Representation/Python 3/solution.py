class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        seen = {}
        result = 0
        
        for num in range(L, R + 1):
            bits = bin(num).count('1')
            if bits not in seen:
                seen[bits] = self.isPrime(bits)
            
            result += seen[bits]
        
        return result
    
    def isPrime(self, num):
        if num == 1 or num == 0:
            return 0
        
        for cnt in range(2, int(math.sqrt(num)) + 1):
            if num % cnt == 0:
                return 0
            
        return 1
        