class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        if not seqs:
            return False
        graph = collections.defaultdict(set)
        degrees = collections.Counter()
        size = len(org)
        for seq in seqs:
            if not seq:
                continue
            seq_size = len(seq)
            degrees[seq[0]] += 0
            for idx in range(1, seq_size):
                if seq[idx] not in graph[seq[idx - 1]]:
                    graph[seq[idx - 1]].add(seq[idx])
                    degrees[seq[idx]] += 1

        queue = collections.deque(x for x in degrees if degrees[x] == 0)
        result = []
        while len(queue) == 1:
            cur = queue.popleft()
            result.append(cur)
            for nxt in graph[cur]:
                degrees[nxt] -= 1
                if degrees[nxt] == 0:
                    queue.append(nxt)

        if len(queue) > 1:
            return False

        return org == result and len(degrees.keys()) == len(org)
