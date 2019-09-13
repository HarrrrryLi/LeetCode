class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        record = {}
        seen = set()
        result = 1
        for num in nums:
            if num not in seen:
                temp = 0
                temp_num = num
                visited = set()
                while nums[temp_num] != temp_num:
                    if temp_num in record:
                        temp += record[temp_num]
                        break
                    if temp_num in visited:
                        break
                    visited.add(temp_num)
                    seen.add(temp_num)
                    temp_num = nums[temp_num]
                    temp += 1
                record[num] = temp
                result = max(result, temp)

        return result
