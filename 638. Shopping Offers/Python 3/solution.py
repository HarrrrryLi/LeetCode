class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        psize = len(price)
        queue = collections.deque()
        queue.append((0, needs))
        result = sum([price[i] * needs[i] for i in range(len(price))])
        while queue:
            total, need = queue.popleft()
            if not any(need):
                result = min(result, total)
            if total >= result:
                continue

            for s in special:
                temp = list(need)
                use_offer = True
                for cnt in range(psize):
                    if temp[cnt] < s[cnt]:
                        use_offer = False
                        break
                    temp[cnt] -= s[cnt]
                if use_offer:
                    queue.append((total + s[-1], temp))
                else:
                    temp_t = total
                    for cnt in range(psize):
                        temp_t += need[cnt] * price[cnt]
                    result = min(result, temp_t)

        return result
