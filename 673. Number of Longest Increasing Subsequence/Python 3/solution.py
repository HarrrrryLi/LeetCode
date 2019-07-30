class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        dp = [1] * size
        length_record = [1] * size
        max_length, freq = 1, 1
        for cnt in range(1, size):
            num = nums[cnt]
            temp_cnt = 1
            temp_length = 1
            for reverse_cnt in range(cnt - 1, -1, -1):
                if nums[reverse_cnt] < num:
                    if dp[cnt] < dp[reverse_cnt] + 1:
                        temp_length = dp[reverse_cnt] + 1
                        dp[cnt] = temp_length
                        temp_cnt = length_record[reverse_cnt]
                    elif dp[cnt] == dp[reverse_cnt] + 1:
                        temp_cnt += length_record[reverse_cnt]

            length_record[cnt] = temp_cnt
            if temp_length > max_length:
                freq = temp_cnt
                max_length = temp_length
            elif temp_length == max_length:
                freq += temp_cnt
        return freq
