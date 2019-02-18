class Solution(object):    
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        size = len(heights)
        self.leftheap = []
        self.rightheap = []
        
        left = self.moveleft(heights, K)
        right = self.moveright(heights, K)
        
        
        for _ in range(V):
            if self.leftheap and self.leftheap[0][0] < heights[K]:
                height, idx = heapq.heappop(self.leftheap)
                idx = -idx
                heights[idx] += 1
                heapq.heappush(self.leftheap, (heights[idx], -idx))
                if left == idx:
                    left = self.moveleft(heights, left)
            elif self.rightheap and self.rightheap[0][0] < heights[K]:
                height, idx = heapq.heappop(self.rightheap)
                heights[idx] += 1
                heapq.heappush(self.rightheap, (heights[idx], idx))
                if right == idx:
                    right = self.moveright(heights, right)
            else:
                heights[K] += 1
                if left == K:
                    left = self.moveleft(heights, left)
                if right == K:
                    right = self.moveright(heights, right)
            
        return heights
        
    def moveleft(self, heights, l):
        while l > 0 and heights[l] >= heights[l - 1]:
            l -= 1
            heapq.heappush(self.leftheap, (heights[l], -l))
        return l
    
    def moveright(self, heights, r):
        while r < len(heights) - 1 and heights[r] >= heights[r + 1]:
            r += 1
            heapq.heappush(self.rightheap, (heights[r], r))
        return r
        