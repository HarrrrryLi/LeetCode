class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:

        temp = dict()
        for idx, num in enumerate(arr2):
            temp[num] = idx

        result = sorted(arr1, key=lambda x: (temp.get(x, len(arr2)), x))

        return result
