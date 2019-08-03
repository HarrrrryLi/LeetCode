class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        size = len(A)
        A.sort()
        Cnter = collections.Counter(A)
        result = 0
        candidates = set()
        pre = -1
        cnt1 = 0

        while cnt1 < size:
            num1 = A[cnt1]
            while num1 == pre:
                cnt1 += 1
                num1 = A[cnt1]
            left = cnt1 + 1
            right = size - 1
            while left < right:
                _sum = A[left] + A[right] + num1
                if _sum < target:
                    temp = left + 1
                    while temp < right and A[temp] == A[left]:
                        temp += 1
                    left = temp
                elif _sum > target:
                    temp = right - 1
                    while temp > left and A[temp] == A[right]:
                        temp -= 1
                    right = temp
                else:
                    candidates.add((num1, A[left], A[right]))
                    if A[left] == A[right]:
                        break
                    else:
                        temp = left + 1
                        while temp < right and A[temp] == A[left]:
                            temp += 1
                        left = temp
                        temp = right - 1
                        while temp < left and A[temp] == A[right]:
                            temp -= 1
                        right = temp
            cnt1 += 1

        for candidate in candidates:
            temp_cnter = collections.Counter(candidate)
            temp = 1
            for key in temp_cnter:
                temp *= self.choose(temp_cnter[key], Cnter[key])
            result += temp

        return result % (10 ** 9 + 7)

    def choose(self, r, n):
        result = 1
        for cnt in range(r):
            result *= (n - cnt)
        for cnt in range(2, r + 1):
            result //= cnt
        return result
