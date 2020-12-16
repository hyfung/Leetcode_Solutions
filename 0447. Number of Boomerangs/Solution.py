class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        import math
        N = len(points)
        distances = dict()
        
        def dist(a, b):
            return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
        
        # Get all distances
        for i in range(N):
            for j in range(i+1, N):
                distances[(i,j)] = dist(points[i], points[j])
        
        group = dict()
        # Group points by distances
        for v in distances.values():
            if v not in group:
                group[v] = 1
            else:
                group[v] += 1
        
        number = 0
        for v in group.values():
            if v > 1:
                number += math.factorial(v) / math.factorial(v-2)
        
        
        print(distances)
        print(group)
                
        return int(number)
        
