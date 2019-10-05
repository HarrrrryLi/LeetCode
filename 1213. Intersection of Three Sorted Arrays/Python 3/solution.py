class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        size1, size2, size3 = len(arr1), len(arr2), len(arr3)
        ptr1, ptr2, ptr3 = 0, 0, 0

        result = []

        while ptr1 < size1 and ptr2 < size2 and ptr3 < size3:
            num1, num2, num3 = arr1[ptr1], arr2[ptr2], arr3[ptr3]
            max_num = max(num1, num2, num3)
            if num1 == num2 and num1 == num3:
                ptr1 += 1
                ptr2 += 1
                ptr3 += 1
                result.append(num1)
            else:
                if num1 < max_num:
                    ptr1 += 1
                if num2 < max_num:
                    ptr2 += 1
                if num3 < max_num:
                    ptr3 += 1

        return result
