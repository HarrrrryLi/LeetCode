class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        dx = {-1: 0}

        for a in arr1:
            ndx = {}
            for x, d in dx.items():
                if a > x:
                    ndx[a] = min(ndx.get(a, float('inf')), d)
                i = bisect.bisect(arr2, x)
                if i < len(arr2):
                    ndx[arr2[i]] = min(ndx.get(arr2[i], float('inf')), d + 1)
            dx = ndx
        return -1 if not dx else min(dx.values())
