class Solution:
    def balancedString(self, s: str) -> int:
        size = len(s)
        target = size // 4
        Cnter = collections.Counter(s)
        target_sub = collections.Counter()
        for key in Cnter:
            if Cnter[key] > target:
                target_sub[key] = Cnter[key] - target

        if not target_sub:
            return 0

        left, right = 0, 0
        current = collections.Counter()
        count = 0
        result = size
        while right < size:
            if s[right] in target_sub:
                current[s[right]] += 1
                if current[s[right]] == target_sub[s[right]]:
                    count += 1
                if count == len(target_sub):
                    result = min(result, right + 1 - left)
                if current[s[right]] > target_sub[s[right]]:
                    while left < right:
                        if s[left] in target_sub:
                            if current[s[left]] > target_sub[s[left]]:
                                current[s[left]] -= 1
                            else:
                                break
                        left += 1
                    if count == len(target_sub):
                        result = min(result, right + 1 - left)

            right += 1
        return result
