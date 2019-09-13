class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        record1 = {word: idx for idx, word in enumerate(list1)}
        record2 = {word: idx for idx, word in enumerate(list2)}

        max_idx = len(list1) + len(list2)
        result = []
        for key in record1:
            if key in record2:
                _sum = record1[key] + record2[key]
                if _sum < max_idx:
                    max_idx = _sum
                    result = []
                    result.append(key)
                elif _sum == max_idx:
                    result.append(key)

        return result
