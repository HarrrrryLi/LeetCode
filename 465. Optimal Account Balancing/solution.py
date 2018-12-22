class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        record = collections.defaultdict(int)
        for sender, receiever, amount in transactions:
            record[sender] -= amount
            record[receiever] += amount
        
        amounts = [record[p] for p in record if record[p] != 0]
        result = len(amounts)
        
        while amounts:
            size = len(amounts)
            queue = collections.deque()
            queue.append(([0],amounts[0]))
            while queue:
                people, total = queue.popleft();
                if total == 0:
                    amounts = [a for i, a in enumerate(amounts) if i not in set(people)]
                    result -= 1
                    break
                for cnt in range(people[-1] + 1, size):
                    queue.append((people + [cnt], total + amounts[cnt]))
        
        return result