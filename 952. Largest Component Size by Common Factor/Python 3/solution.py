from collections import defaultdict

# to factorize k numbers below N, if k is almost as big as N,
# it is more efficient to factorize all numbers by sieving
# to save space, only keep an array of the smallest factor for each number


def factorList(n):
    lst = [0]*(n+1)
    lst[1] = 1
    for i in range(2, n+1):
        if lst[i] == 0:
            for j in range(i, n+1, i):
                lst[j] = i
    return lst


def factors(faclist, n):
    while n > 1:
        curr = faclist[n]
        yield curr
        n //= curr

# union find from https://medium.com/100-days-of-algorithms/day-41-union-find-d0027148376d
# with path compression


def find(data, i):
    if i != data[i]:
        data[i] = find(data, data[i])
    return data[i]


def union(data, i, j):
    pi, pj = find(data, i), find(data, j)
    if pi != pj:
        data[pi] = pj


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        faclist = factorList(max(A))
        # for each prime number save a
        # representative, so that we have
        # a candidate to "union" on
        repre = {}
        data = {x: x for x in A}
        for n in A:
            for fac in factors(faclist, n):
                if fac in repre:
                    union(data, n, repre[fac])
                else:
                    repre[fac] = n
        counter = defaultdict(lambda: 0)
        for n in A:
            counter[find(data, n)] += 1
        return max(counter.values())
