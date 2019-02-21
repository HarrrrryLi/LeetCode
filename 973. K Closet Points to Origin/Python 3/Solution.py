class Solution:
    def kClosest(self, points: 'List[List[int]]', K: 'int') -> 'List[List[int]]':
        points.sort(key=lambda x: self.get_distance2(x))
        return points[:K]
    
    
    def get_distance2(self, point: 'List[int]') -> 'int':
        return point[0] * point[0] + point[1] * point[1]
        