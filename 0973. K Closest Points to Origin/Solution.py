class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        import math
        def distance_square(point):
            return (point[0] ** 2 + point[1] ** 2)
        
        distances = dict()
        
        for i, point in enumerate(points):
            distances[i] = distance_square(point)
        
        distances = sorted(list(distances.items()), key=lambda x:x[1])
        
        target_index = [x[0] for x in distances][:K]

        res = []
        for v in target_index:
            res.append(points[v])
        
        return res
        
