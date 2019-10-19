class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        size1, size2 = len(slots1), len(slots2)
        slots1.sort()
        slots2.sort()
        ptr1, ptr2 = 0, 0
        result = []
        while ptr1 < size1 and ptr2 < size2:
            start1, end1 = slots1[ptr1]
            while ptr1 < size1 and end1 - start1 < duration:
                ptr1 += 1
                if ptr1 < size1:
                    start1, end1 = slots1[ptr1]
            if ptr1 == size1:
                break

            start2, end2 = slots2[ptr2]
            while ptr2 < size2 and end2 - start2 < duration:
                ptr2 += 1
                if ptr2 < size2:
                    start2, end2 = slots2[ptr2]
            if ptr2 == size2:
                break

            if start1 + duration > end2:
                ptr2 += 1
            elif start2 + duration > end1:
                ptr1 += 1
            else:
                result = [max(start1, start2), max(start1, start2) + duration]
                break

        return result
