class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        s = set()
        
        for i,v in enumerate(intervals):
            
            for i_, v_ in enumerate(intervals):
                if v[0] >= v_[0] and v[1] <= v_[1]:
                    intervals[i][0] = v_[0]
                    intervals[i][1] = v_[1]
        
        for i in intervals:
            s.add((i[0], i[1]))
        
        return len(s)
