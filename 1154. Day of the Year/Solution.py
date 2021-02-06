class Solution:
    def dayOfYear(self, date: str) -> int:
        def isLeapYear(yr):
            if yr % 4 == 0:
                if yr % 100 == 0:
                    if yr % 400 == 0:
                        return True
                else:
                    return True
            else:
                return False
        
        leap = [0,0,31,60,91,121,152,182,213,244,274,305,335,366]
        not_leap = [0,0,31,59,90,120,151,181,212,243,273,304,334,365]
        
        yy,mm,dd = date.split("-")
        
        if isLeapYear(int(yy)):
            return leap[int(mm)] + int(dd)
        else:
            return not_leap[int(mm)] + int(dd)
        
