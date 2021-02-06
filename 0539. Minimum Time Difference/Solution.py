class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        normalized = []
        
        for i in timePoints:
            h,m = i.split(':')
            normalized.append(int(h)*60+int(m))
            normalized.append(int(h)*60+int(m)+1440)
        
        normalized.sort()
        
        min_diff = 2147483647
        for i in range(len(normalized) - 1):
            tmp = normalized[i+1] - normalized[i]
            min_diff = tmp if tmp < min_diff else min_diff
            
        return min_diff
        
