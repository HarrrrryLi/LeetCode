class Solution:
    def lengthLongestPath(self, input: str) -> int:
        d = {}
        result = 0
        fileList = input.split('\n')

        for f in fileList:
            if '.' not in f:
                key = f.count('\t')
                d[key] = len(f.replace('\t', ''))
            else:
                key = f.count('\t')
                temp = 0
                for cnt in range(key):
                    temp += d[cnt]
                temp += len(f.replace('\t', '')) + key
                result = max(temp, result)

        return result
