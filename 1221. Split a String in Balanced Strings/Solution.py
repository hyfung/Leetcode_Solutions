class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        l_cnt, r_cnt = 0, 0
        ret = 0
        
        for ch in s:
            if ch == 'L':
                l_cnt += 1
            if ch == 'R':
                r_cnt += 1
            if l_cnt == r_cnt:
                ret += 1
                l_cnt, r_cnt = 0, 0
        
        return ret
        
