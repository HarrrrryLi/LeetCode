class MajorityChecker(object):

    def __init__(self, A):
        a2i = collections.defaultdict(list)
        for i, x in enumerate(A):
            a2i[x].append(i)
        self.A, self.a2i = A, a2i

    def query(self, left, right, threshold):
        # visited = set()
        # for cnt in range(left, right + 1):
        #     if cnt in visited:
        #         continue
        #     visited.add(cnt)
        #     a = self.A[cnt]
        #     indices = self.a2i[a]
        #     l = bisect.bisect_left(indices, left)
        #     r = bisect.bisect_right(indices, right)
        #     if r - l >= threshold:
        #         return a
        for _ in range(20):
            a = self.A[random.randint(left, right)]
            indices = self.a2i[a]
            l = bisect.bisect_left(indices, left)
            r = bisect.bisect_right(indices, right)
            if r - l >= threshold:
                return a
        return -1
        


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)