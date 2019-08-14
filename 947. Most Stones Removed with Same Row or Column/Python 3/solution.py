class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = dict()
        count = 0
        rows = dict()
        cols = dict()

        def find(r, c):
            if parent[r, c] != parent[parent[r, c]]:
                parent[r, c] = find(parent[r, c][0], parent[r, c][1])
            return parent[r, c]

        def union(r1, c1, r2, c2):
            p1 = find(r1, c1)
            p2 = find(r2, c2)
            parent[p2] = p1

        for r, c in stones:
            if r in rows:
                parent[r, c] = find(r, rows[r])
                if c in cols and find(cols[c], c) != parent[r, c]:
                    union(r, c, cols[c], c)
                    count -= 1
            elif c in cols:
                parent[r, c] = find(cols[c], c)
            else:
                parent[r, c] = (r, c)
                count += 1

            if r not in rows:
                rows[r] = c
            if c not in cols:
                cols[c] = r

        return len(stones) - count
