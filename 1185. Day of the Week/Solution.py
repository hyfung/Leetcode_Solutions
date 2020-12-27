class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        import time
        
        t = (year, month, day, 0, 0, 1, 0, 0, 0)
        
        t = time.mktime(t)
        
        i = time.gmtime(t).tm_wday
        
        return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][i]
        
